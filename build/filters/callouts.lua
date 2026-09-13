-- callouts.lua
-- Pandoc Lua filter: convert fenced divs into paragraphs with callout styles
-- Usage (markdown):
--   ::: {.note}
--   **NOTE:** content
--   :::
--
-- Recognised classes: note, warning, definition, example, safety, tip
-- Mapped to Word paragraph styles: Callout Note / Callout Warning / Callout
-- Definition / Callout Example. `safety` is aliased to Warning, `tip` to Note.

local class_to_style = {
  note        = "Callout Note",
  tip         = "Callout Note",
  warning     = "Callout Warning",
  safety      = "Callout Warning",
  caution     = "Callout Warning",
  definition  = "Callout Definition",
  def         = "Callout Definition",
  example     = "Callout Example",
  pullquote   = "Pull Quote",
  pull        = "Pull Quote",
}

local class_to_label = {
  note        = "NOTE",
  tip         = "TIP",
  warning     = "WARNING",
  safety      = "SAFETY",
  caution     = "CAUTION",
  definition  = "DEFINITION",
  def         = "DEFINITION",
  example     = "EXAMPLE",
  pullquote   = nil,  -- no auto-label for pull quotes
  pull        = nil,
}

function Div(el)
  local style = nil
  local label = nil
  for _, cls in ipairs(el.classes) do
    if class_to_style[cls] then
      style = class_to_style[cls]
      label = class_to_label[cls]
      break
    end
  end
  if not style then return nil end

  -- Skip auto-label insertion when label is nil (e.g. pull quotes).
  local has_label = (label == nil)
  if not has_label and #el.content > 0 and el.content[1].t == "Para" then
    local first_inlines = el.content[1].content
    if #first_inlines > 0 then
      local first = first_inlines[1]
      if first.t == "Strong" and first.content and #first.content > 0 then
        local txt = pandoc.utils.stringify(first.content):upper()
        if txt:find(label, 1, true) then
          has_label = true
        end
      end
    end
  end

  if not has_label then
    local label_inlines = {
      pandoc.Strong({ pandoc.Str(label .. ":") }),
      pandoc.Space(),
    }
    if #el.content > 0 and el.content[1].t == "Para" then
      for _, inl in ipairs(el.content[1].content) do
        table.insert(label_inlines, inl)
      end
      el.content[1] = pandoc.Para(label_inlines)
    else
      table.insert(el.content, 1, pandoc.Para(label_inlines))
    end
  end

  -- Apply the callout paragraph style to every block paragraph inside.
  for i, blk in ipairs(el.content) do
    if blk.t == "Para" or blk.t == "Plain" then
      el.content[i] = pandoc.Div(
        { pandoc.Para(blk.content) },
        pandoc.Attr("", {}, { ["custom-style"] = style })
      )
    end
  end

  return el.content
end
