# Teacher guide and content review

Use fictional examples throughout. Students may prefer not to discuss death or family finances; let them work with Maya and Leo's examples instead. Each lesson can fill one 45–60 minute session: about 10 minutes for the story and predictions, 15 for the demo, 20 for practice, and 5 for reflection.

The arithmetic checks in each notebook validate the supplied examples, not arbitrary student answers. Read student code and explanations as well: passing the supplied assertions does not mean a student completed the exercise. Sample solutions are intentionally visible after the hints; ask students to attempt the workspace first.

## Expected results and exit-ticket discussion

| Lesson | Expected result | Exit-ticket guidance |
|---|---|---|
| 01 | Three printed demo messages; comments do not print. | Quotes delimit text; # starts a comment. The insured person and payer can be different people. |
| 02 | ₱4,200 versus ₱4,000; challenge ₱5,100 versus ₱4,900. Both differences are ₱200. | * multiplies. More premiums do not automatically imply a larger benefit. |
| 03 | ₱300,000 and ₱200,000; challenge ₱200,000 and ₱600,000; shares sum to 100%. | Python lists start at index 0. A beneficiary is a chosen recipient, subject to policy and legal rules. |
| 04 | Before start: False; exact start: True; exact end: False. | A boolean is True or False. The example window is start-inclusive and end-exclusive. Policy status, exclusions, and other terms still matter. |
| 05 | Original expenses ₱16,850, remainder ₱3,150; revised expenses ₱18,050, remainder ₱1,950. | Copying preserves the original dictionary. Premiums compete with other expenses in a budget. |
| 06 | Budget matches Oak/River; coverage challenge matches River/Sky. | and requires both conditions. Exclusions, eligibility, payment and renewal rules are omitted. |
| 07 | Annual premium ₱4,200; demo gap ₱400,000; challenge gaps ₱500,000, ₱0, ₱0. | return supplies a value for reuse; print displays it. An estimated gap does not price risk or determine a premium. |
| 08 | P001 and P006 accepted; four records flagged; accepted monthly total ₱950. | Missing data means unknown, not zero. Guessing can misrepresent a payment obligation. These checks do not establish active coverage. |
| 09 | Ten-year totals ₱30,000 and ₱42,000; differences ₱6,000 at year 5 and ₱12,000 at year 10. | Index 0 is year 0. Payments accumulated are not a benefit amount, account balance, or suitability measure. |
| 10 | ₱400 matches Oak/River; ₱600 with minimum coverage ₱500,000 matches River/Sky. Demo quiz 3/3; practice 2/3. | Negative, nonnumeric, missing, and nonfinite budgets are tested. Exclusions and eligibility are examples of omitted policy details. |

## Accuracy review

- The insured person, premium payer, and beneficiary are distinguished rather than assumed to be the same person.
- Benefits are conditional on a covered death and policy terms; examples do not promise claim approval.
- Term coverage is limited to a stated period, with an explicit classroom date-boundary convention.
- Premium schedules, beneficiary rules, and renewals are described as policy-dependent.
- Fixed-price premium projections explicitly assume all scheduled payments occur and prices remain unchanged.
- The coverage-gap estimate is clamped at zero and explicitly omits real-world planning factors.
- Missing and invalid records are flagged rather than replaced with invented values; the original CSV is preserved.
- Chart axes describe payments, not savings or benefits; policy filters do not imply recommendations or eligibility.
- All prices and datasets are invented. PHP units do not imply legal or product accuracy for any jurisdiction.

This is an educational content review, not a legal review or certification by an insurance professional. Before using the material to explain a particular real policy, have an appropriately qualified person check that policy's wording.
