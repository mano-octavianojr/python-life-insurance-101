# Python through life insurance: 10-notebook learning plan

## Goal

Create 10 Jupyter notebooks that teach high school students to code in Python while introducing life insurance in plain, everyday language. No prior programming or insurance knowledge is required.

## Continuing story

Maya, a high school student, helps her fictional family understand life insurance while learning Python. Her friend Leo joins her. Each notebook opens with a short story, uses code to answer a practical question, and ends with what the characters learned.

Introduce life insurance as an agreement: a person pays an insurer, and the insurer pays money to the chosen recipient if the insured person dies while covered, subject to the policy's terms.

All people, prices, policies, and records are fictional teaching examples. Use Philippine pesos (₱) consistently in examples. Explain concepts without assuming that every policy or country follows the same rules.

## Notebook sequence

| # | Notebook and story | Insurance concept in everyday words | Python learning goals | Demo and student challenge |
|---|---|---|---|---|
| 1 | **Meet Maya: Your First Python Program.** Maya hears about life insurance at dinner and introduces her fictional family. | The **insured person** is the person whose life is covered. | `print()`, comments, strings. | Print a character introduction and a simple explanation of life insurance. Create another fictional character. |
| 2 | **The Monthly Payment Mystery.** Maya notices an insurance payment in the family budget. | A **premium** is the payment made to keep insurance coverage going. | Variables, numbers, arithmetic, f-strings. | Calculate yearly payments from a monthly premium. Compare monthly and annual payment options using supplied fictional prices. |
| 3 | **Who Receives the Money?** Maya learns that her aunt selected two people to receive a payout. | A **beneficiary** is a person chosen to receive the insurance money. | Lists, indexing, dictionaries. | Store names and shares and calculate how a fictional payout is divided. Check that the shares total 100%. |
| 4 | **Coverage Has a Calendar.** Leo discovers that a policy covers a fixed number of years. | **Term life insurance** provides coverage for a set period, such as 10 or 20 years. | Booleans, comparisons, `if` / `elif` / `else`. | Check whether a hypothetical date falls within a coverage period. Test dates before, during, and after it. Explain that dates alone do not determine whether a real claim is payable. |
| 5 | **Maya Builds a Budget.** Maya explores how premiums fit alongside food, transport, and other expenses. | Insurance payments are one part of a household budget. | Dictionaries, loops, totals. | Add monthly expenses and calculate money left over. Change the fictional budget and explain the effect. |
| 6 | **The Policy Comparison Club.** Maya and Leo compare three fictional policies for a school project. | The **coverage amount** is the amount a policy promises to pay for a covered death. | Lists of dictionaries, iteration, filtering. | Display premiums, coverage amounts, and terms. Find policies within a budget and explain why the cheapest policy is not automatically the best fit. |
| 7 | **A Calculator That Can Be Reused.** Maya turns repeated calculations into reusable tools. | A **coverage gap** is the difference between a hypothetical money need and resources already available. | Functions, parameters, return values. | Write functions for annual premiums and a simplified coverage-gap estimate. Try several fictional households; explain that the estimate is a classroom exercise, not financial advice. |
| 8 | **Fixing the Messy Records.** The school club receives a fictional spreadsheet with blank names, negative payments, and numbers stored as text. | Accurate records help people understand their policies and payments. | pandas, CSV files, missing values, basic validation. | Load and clean synthetic policy records. Identify invalid entries and explain why guessing missing information can cause problems. |
| 9 | **Tell the Story with Charts.** Maya presents how premiums accumulate over time. | **Total premiums paid** and an **insurance payout** are different quantities. | matplotlib, chart labels, interpreting data. | Plot cumulative premiums for two fictional term policies. Explain what the chart shows and what it cannot tell us about policy suitability. |
| 10 | **Maya's Insurance Learning Fair.** Maya and Leo create an educational tool for classmates. | Review premiums, beneficiaries, term coverage, and coverage amounts. | Combining functions, data handling, input validation, simple assertions. | Build a policy explorer that accepts a budget, displays matching fictional policies, calculates premium totals, and offers a short quiz. Add one feature and explain its limitations. |

## Structure of every notebook

1. **Story opening:** a short scene and a concrete question to solve.
2. **Learning goals:** a few clear Python and insurance outcomes.
3. **Insurance in everyday words:** introduce one or two terms with a relatable example.
4. **Predict, then run:** ask students to predict the output of a small code cell.
5. **Guided demo:** explain and execute code in manageable steps.
6. **Your turn:** modify an example, then solve a small challenge.
7. **Story ending:** explain what Maya and Leo learned.
8. **Exit ticket:** one coding question and one insurance question.

Provide hints and clearly separated sample solutions so students can attempt exercises first. Introduce tools before asking students to use them, and include plain-language explanations of common errors.

## Example: Notebook 2

> Maya notices a fictional insurance premium of ₱350 per month. “How much would that be over a whole year?” she asks. Let's help her calculate it.

```python
monthly_premium = 350
months_in_year = 12

annual_premium = monthly_premium * months_in_year

print(f"The premiums total ₱{annual_premium:,} over one year.")
```

Students change the monthly premium and predict the new result before running the cell.

## Teaching principles

- Keep the story warm, practical, and age-appropriate; discuss death sensitively without graphic scenarios.
- Explain insurance terms when first introduced and reinforce them through examples.
- Use fictional families and synthetic data. Do not ask students to share personal family finances or health information.
- Keep examples educational: do not recommend real policies, imply guaranteed eligibility, or present simplified calculations as professional advice.
- Separate premiums paid from benefits payable. Explain that actual coverage depends on policy terms.
- Keep early notebooks focused on Python's standard library; introduce pandas and matplotlib only when the lessons need them.

## Implementation checklist

- [x] Create 10 numbered `.ipynb` files following the sequence above.
- [x] Write each story, plain-language explanation, guided demo, exercise, hint, and sample solution.
- [x] Supply local synthetic data for the records and chart lessons.
- [x] Document how to install Jupyter, pandas, and matplotlib and open the notebooks.
- [x] Execute completed demonstration and solution cells from fresh kernels in order; confirm expected outputs and correct deliberate-error examples.
- [x] Ensure student exercise placeholders are clearly marked and do not cause unexplained failures during a full notebook run.
- [x] Review insurance explanations for accuracy, accessibility, and consistency.
- [x] Confirm notebooks work without credentials, external services, or personal data.

## Completion criteria

Students can progress from printing their first message to demonstrating a small policy explorer, explain the insurance concepts in their own words, and distinguish classroom examples from real policy decisions. Each notebook has a complete story and can be opened and used with the documented setup.

The ten notebooks are implemented. See README.md for setup, TEACHER_GUIDE.md for expected results and content-review notes, and scripts/validate_notebooks.py for execution checks.
