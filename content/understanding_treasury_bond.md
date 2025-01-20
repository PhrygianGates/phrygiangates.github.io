+++
date = '2025-01-20T02:52:00-05:00'
katex = true
title = 'Understanding Treasury Bonds'
tags = ['Investment']
+++

I would like to learn some basic information about treasury bonds. The following questions are of interest to me:
1. How the coupon rate is determined?
2. How the yield is determined?
3. What's the relationship between yield and price? 
4. The relationship between yield and interest rate? 
5. From a macroeconomic perspective, what's the status of the treasury bond market of USA, China, and Japan?

We will refer to [these lectures](https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/pages/video-lectures-and-slides/fixed-income-securities/)


Treasury bonds are fixed-income securities issued by governments to finance expenditures. Their value and yields are essential for investors and play a critical role in macroeconomic analysis. Below are organized and extended insights based on the provided questions.

---

### 1. **Coupon Rate**

The **coupon rate** is the annual interest rate paid by the bond issuer on the bond’s face value. It is expressed as a percentage and is determined at issuance based on:

- **Market Interest Rates**: When a bond is issued, its coupon rate is designed to align with prevailing interest rates to attract investors.
- **Creditworthiness of the Issuer**: Higher perceived risk requires a higher coupon rate to compensate investors.
- **Economic Conditions**: Inflation expectations and macroeconomic stability influence coupon rates.

#### Example:

If a bond’s face value is $1,000 and the coupon rate is 5%, the annual payment to the investor will be $50.

---

### 2. **How Yield Is Determined**

The **yield** represents the return an investor earns on a bond and varies with the bond’s price.

- **Yield to Maturity (YTM)**: The total return if the bond is held to maturity, considering all coupon payments and capital gains or losses.

#### Yield Formula for a Bond:

Where:

- **Bond’s current price (\\(P_0\\))**: This is **deduced** based on market dynamics, coupon payments, and yield.
- **Annual coupon payment (\\(C\\))**: This is **set** during the bond’s design based on the coupon rate and face value.
- **Face value (\\(F\\))**: This is **set** and represents the amount repaid to the bondholder at maturity.
- **Yield to maturity (\\(y\\))**: This is **deduced** as the rate of return considering all payments and the bond’s price.
- **Time to maturity (\\(T\\))**: This is **set** when the bond is issued and reflects the bond’s term.

#### Example:

Suppose a bond has the following characteristics:

- Face value (\\(F\\)): $1,000
- Annual coupon payment (\\(C\\)): $50 (5% of face value)
- Time to maturity (\\(T\\)): 3 years
- Yield to maturity (\\(y\\)): 4% or 0.04 (Assumed for illustration purposes. YTM is typically deduced from market prices, but here it serves as a reference to simplify the example.)

Using the yield formula:
\\[
P_0 = \frac{C}{(1+y)^1} + \frac{C}{(1+y)^2} + \frac{C+F}{(1+y)^3}
\\]

#### Calculations:
1. First year payment:
\\[
\frac{50}{(1+0.04)^1} = \frac{50}{1.04} = 48.08
\\]
2. Second year payment:
\\[
\frac{50}{(1+0.04)^2} = \frac{50}{1.0816} = 46.23
\\]
3. Third year payment (including face value):
\\[
\frac{1050}{(1+0.04)^3} = \frac{1050}{1.124864} = 933.51
\\]

#### Add them together:
\\[
P_0 = 48.08 + 46.23 + 933.51 = 1,027.82
\\]

The bond’s current price is **$1,027.82** when the yield to maturity is 4%.

Normally, in real-world scenarios, the market determines the price of a bond through supply and demand. Once the price is observed, the Yield to Maturity (YTM) can be deduced as the rate of return that equates the bond’s future cash flows (coupon payments and face value) to its current market price.

---

### 4. **Relationship Between Yield and Interest Rate**

Interest rates influence both the design of the coupon rate at issuance and the bond’s yield in secondary markets.

- **Coupon Rate Determination**: When interest rates are high, new bonds are issued with higher coupon rates to remain competitive.
- **Yield Adjustments**: Changes in interest rates directly impact bond prices, leading to adjustments in yields.

#### Key Points:

- **Rising interest rates** lead to lower bond prices and higher yields.
- **Falling interest rates** lead to higher bond prices and lower yields.


