#!/usr/bin/env bash
# One-shot rename of tuinalogy WIM files: code-only -> code + descriptive suffix.
# Run from repo root. Idempotent: skips if source missing.
set -e
cd "$(dirname "$0")/.."

mv_one() {
    local src="$1" dst="$2"
    if [ -f "$src" ]; then
        git mv "$src" "$dst"
    elif [ -f "$dst" ]; then
        echo "skip (already renamed): $dst"
    else
        echo "MISSING: $src" >&2
    fi
}

# C01 — Customer Consultation & Service Planning
mv_one tuinalogy-services/C01/KP-01.md tuinalogy-services/C01/KP-01-consultation-area-reception.md
mv_one tuinalogy-services/C01/KP-02.md tuinalogy-services/C01/KP-02-client-tcm-four-diagnostics.md
mv_one tuinalogy-services/C01/KP-03.md tuinalogy-services/C01/KP-03-indications-contraindications-referral.md
mv_one tuinalogy-services/C01/KP-04.md tuinalogy-services/C01/KP-04-service-plan-design.md
mv_one tuinalogy-services/C01/KT-01.md tuinalogy-services/C01/KT-01-consultation-area-reception.md
mv_one tuinalogy-services/C01/KT-02.md tuinalogy-services/C01/KT-02-client-tcm-four-diagnostics.md
mv_one tuinalogy-services/C01/KT-03.md tuinalogy-services/C01/KT-03-indications-contraindications-referral.md
mv_one tuinalogy-services/C01/KT-04.md tuinalogy-services/C01/KT-04-service-plan-design.md
mv_one tuinalogy-services/C01/KK-01.md tuinalogy-services/C01/KK-01-consultation-area-reception.md
mv_one tuinalogy-services/C01/KK-02.md tuinalogy-services/C01/KK-02-client-tcm-four-diagnostics.md
mv_one tuinalogy-services/C01/KK-03.md tuinalogy-services/C01/KK-03-indications-contraindications-referral.md
mv_one tuinalogy-services/C01/KK-04.md tuinalogy-services/C01/KK-04-service-plan-writeup.md
mv_one tuinalogy-services/C01/KA.md tuinalogy-services/C01/KA-client-consultation-service-planning.md
mv_one tuinalogy-services/C01/PA.md tuinalogy-services/C01/PA-client-consultation-service-planning.md
mv_one tuinalogy-services/C01/PM-teori.md tuinalogy-services/C01/PM-teori-client-consultation-service-planning.md
mv_one tuinalogy-services/C01/PM-amali.md tuinalogy-services/C01/PM-amali-client-consultation-service-planning.md

# C02 — Full-Body Tuina Service
mv_one tuinalogy-services/C02/KP-01.md tuinalogy-services/C02/KP-01-service-preparation.md
mv_one tuinalogy-services/C02/KP-02.md tuinalogy-services/C02/KP-02-eight-core-techniques.md
mv_one tuinalogy-services/C02/KP-03.md tuinalogy-services/C02/KP-03-post-service-management.md
mv_one tuinalogy-services/C02/KT-01.md tuinalogy-services/C02/KT-01-service-preparation.md
mv_one tuinalogy-services/C02/KT-02.md tuinalogy-services/C02/KT-02-eight-techniques-execution.md
mv_one tuinalogy-services/C02/KT-03.md tuinalogy-services/C02/KT-03-post-service-referral.md
mv_one tuinalogy-services/C02/KK-01.md tuinalogy-services/C02/KK-01-service-preparation-positioning.md
mv_one tuinalogy-services/C02/KK-02.md tuinalogy-services/C02/KK-02-full-body-tuina-execution.md
mv_one tuinalogy-services/C02/KK-03.md tuinalogy-services/C02/KK-03-post-service-documentation.md
mv_one tuinalogy-services/C02/KA.md tuinalogy-services/C02/KA-full-body-tuina.md
mv_one tuinalogy-services/C02/PA.md tuinalogy-services/C02/PA-full-body-tuina.md
mv_one tuinalogy-services/C02/PM-teori.md tuinalogy-services/C02/PM-teori-full-body-tuina.md
mv_one tuinalogy-services/C02/PM-amali.md tuinalogy-services/C02/PM-amali-full-body-tuina.md

# C03 — Sports Tuina Service
mv_one tuinalogy-services/C03/KP-01.md tuinalogy-services/C03/KP-01-principles-injury-assessment.md
mv_one tuinalogy-services/C03/KP-02.md tuinalogy-services/C03/KP-02-techniques-application.md
mv_one tuinalogy-services/C03/KP-03.md tuinalogy-services/C03/KP-03-recovery-management-referral.md
mv_one tuinalogy-services/C03/KT-01.md tuinalogy-services/C03/KT-01-assessment-preparation.md
mv_one tuinalogy-services/C03/KT-02.md tuinalogy-services/C03/KT-02-techniques-application.md
mv_one tuinalogy-services/C03/KT-03.md tuinalogy-services/C03/KT-03-post-service-referral.md
mv_one tuinalogy-services/C03/KK-01.md tuinalogy-services/C03/KK-01-athlete-assessment-preparation.md
mv_one tuinalogy-services/C03/KK-02.md tuinalogy-services/C03/KK-02-pre-post-treatment-execution.md
mv_one tuinalogy-services/C03/KK-03.md tuinalogy-services/C03/KK-03-recovery-followup-advice.md
mv_one tuinalogy-services/C03/KA.md tuinalogy-services/C03/KA-sports-tuina.md
mv_one tuinalogy-services/C03/PA.md tuinalogy-services/C03/PA-sports-tuina.md
mv_one tuinalogy-services/C03/PM-teori.md tuinalogy-services/C03/PM-teori-sports-tuina.md
mv_one tuinalogy-services/C03/PM-amali.md tuinalogy-services/C03/PM-amali-sports-tuina.md

# C04 — Musculoskeletal Tuina Service
mv_one tuinalogy-services/C04/KP-01.md tuinalogy-services/C04/KP-01-musculoskeletal-anatomy.md
mv_one tuinalogy-services/C04/KP-02.md tuinalogy-services/C04/KP-02-common-conditions-techniques.md
mv_one tuinalogy-services/C04/KP-03.md tuinalogy-services/C04/KP-03-rehabilitation-function-assessment.md
mv_one tuinalogy-services/C04/KT-01.md tuinalogy-services/C04/KT-01-anatomy-preparation.md
mv_one tuinalogy-services/C04/KT-02.md tuinalogy-services/C04/KT-02-condition-identification-techniques.md
mv_one tuinalogy-services/C04/KT-03.md tuinalogy-services/C04/KT-03-post-service-rehab-referral.md
mv_one tuinalogy-services/C04/KK-01.md tuinalogy-services/C04/KK-01-msk-assessment.md
mv_one tuinalogy-services/C04/KK-02.md tuinalogy-services/C04/KK-02-regional-tuina-execution.md
mv_one tuinalogy-services/C04/KK-03.md tuinalogy-services/C04/KK-03-functional-recovery-guidance.md
mv_one tuinalogy-services/C04/KA.md tuinalogy-services/C04/KA-musculoskeletal-tuina.md
mv_one tuinalogy-services/C04/PA.md tuinalogy-services/C04/PA-musculoskeletal-tuina.md
mv_one tuinalogy-services/C04/PM-teori.md tuinalogy-services/C04/PM-teori-musculoskeletal-tuina.md
mv_one tuinalogy-services/C04/PM-amali.md tuinalogy-services/C04/PM-amali-musculoskeletal-tuina.md

# C05 — Centre Management & Administration
mv_one tuinalogy-services/C05/KP-01.md tuinalogy-services/C05/KP-01-record-keeping-filing.md
mv_one tuinalogy-services/C05/KP-02.md tuinalogy-services/C05/KP-02-staff-coordination.md
mv_one tuinalogy-services/C05/KP-03.md tuinalogy-services/C05/KP-03-housekeeping-supervision.md
mv_one tuinalogy-services/C05/KP-04.md tuinalogy-services/C05/KP-04-financial-management.md
mv_one tuinalogy-services/C05/KP-05.md tuinalogy-services/C05/KP-05-sales-marketing.md
mv_one tuinalogy-services/C05/KP-06.md tuinalogy-services/C05/KP-06-complaint-management.md
mv_one tuinalogy-services/C05/KT-01.md tuinalogy-services/C05/KT-01-record-keeping-filing.md
mv_one tuinalogy-services/C05/KT-02.md tuinalogy-services/C05/KT-02-staff-coordination.md
mv_one tuinalogy-services/C05/KT-03.md tuinalogy-services/C05/KT-03-housekeeping-supervision.md
mv_one tuinalogy-services/C05/KT-04.md tuinalogy-services/C05/KT-04-financial-management.md
mv_one tuinalogy-services/C05/KT-05.md tuinalogy-services/C05/KT-05-sales-marketing.md
mv_one tuinalogy-services/C05/KT-06.md tuinalogy-services/C05/KT-06-complaint-management.md
mv_one tuinalogy-services/C05/KK-01.md tuinalogy-services/C05/KK-01-record-filing-system.md
mv_one tuinalogy-services/C05/KK-02.md tuinalogy-services/C05/KK-02-staff-scheduling-performance.md
mv_one tuinalogy-services/C05/KK-03.md tuinalogy-services/C05/KK-03-housekeeping-inspection.md
mv_one tuinalogy-services/C05/KK-04.md tuinalogy-services/C05/KK-04-daily-accounting-einvoice.md
mv_one tuinalogy-services/C05/KK-05.md tuinalogy-services/C05/KK-05-sales-marketing-plan.md
mv_one tuinalogy-services/C05/KK-06.md tuinalogy-services/C05/KK-06-complaint-handling-simulation.md
mv_one tuinalogy-services/C05/KA.md tuinalogy-services/C05/KA-centre-management.md
mv_one tuinalogy-services/C05/PA.md tuinalogy-services/C05/PA-centre-management.md
mv_one tuinalogy-services/C05/PM-teori.md tuinalogy-services/C05/PM-teori-centre-management.md
mv_one tuinalogy-services/C05/PM-amali.md tuinalogy-services/C05/PM-amali-centre-management.md

# E01 — Pediatric Tuina
mv_one tuinalogy-services/E01/KP-01.md tuinalogy-services/E01/KP-01-pediatric-physiology-meridians.md
mv_one tuinalogy-services/E01/KP-02.md tuinalogy-services/E01/KP-02-pediatric-techniques-points.md
mv_one tuinalogy-services/E01/KP-03.md tuinalogy-services/E01/KP-03-common-ailments-treatment.md
mv_one tuinalogy-services/E01/KT-01.md tuinalogy-services/E01/KT-01-pediatric-physiology-meridians.md
mv_one tuinalogy-services/E01/KT-02.md tuinalogy-services/E01/KT-02-pediatric-techniques-points.md
mv_one tuinalogy-services/E01/KT-03.md tuinalogy-services/E01/KT-03-common-ailments-referral.md
mv_one tuinalogy-services/E01/KK-01.md tuinalogy-services/E01/KK-01-infant-assessment-parent-communication.md
mv_one tuinalogy-services/E01/KK-02.md tuinalogy-services/E01/KK-02-pediatric-prescription-execution.md
mv_one tuinalogy-services/E01/KK-03.md tuinalogy-services/E01/KK-03-parent-education-followup.md
mv_one tuinalogy-services/E01/KA.md tuinalogy-services/E01/KA-pediatric-tuina.md
mv_one tuinalogy-services/E01/PA.md tuinalogy-services/E01/PA-pediatric-tuina.md
mv_one tuinalogy-services/E01/PM-teori.md tuinalogy-services/E01/PM-teori-pediatric-tuina.md
mv_one tuinalogy-services/E01/PM-amali.md tuinalogy-services/E01/PM-amali-pediatric-tuina.md

# E02 — Women's Tuina
mv_one tuinalogy-services/E02/KP-01.md tuinalogy-services/E02/KP-01-womens-physiology-indications.md
mv_one tuinalogy-services/E02/KP-02.md tuinalogy-services/E02/KP-02-pregnancy-safety-contraindications.md
mv_one tuinalogy-services/E02/KP-03.md tuinalogy-services/E02/KP-03-postpartum-menstrual-menopausal.md
mv_one tuinalogy-services/E02/KT-01.md tuinalogy-services/E02/KT-01-womens-physiology-indications.md
mv_one tuinalogy-services/E02/KT-02.md tuinalogy-services/E02/KT-02-pregnancy-safety-contraindications.md
mv_one tuinalogy-services/E02/KT-03.md tuinalogy-services/E02/KT-03-postpartum-menstrual-menopausal.md
mv_one tuinalogy-services/E02/KK-01.md tuinalogy-services/E02/KK-01-postpartum-practical.md
mv_one tuinalogy-services/E02/KK-02.md tuinalogy-services/E02/KK-02-menstrual-discomfort-practical.md
mv_one tuinalogy-services/E02/KK-03.md tuinalogy-services/E02/KK-03-menopausal-practical.md
mv_one tuinalogy-services/E02/KA.md tuinalogy-services/E02/KA-womens-tuina.md
mv_one tuinalogy-services/E02/PA.md tuinalogy-services/E02/PA-womens-tuina.md
mv_one tuinalogy-services/E02/PM-teori.md tuinalogy-services/E02/PM-teori-womens-tuina.md
mv_one tuinalogy-services/E02/PM-amali.md tuinalogy-services/E02/PM-amali-womens-tuina.md

echo "rename complete"
