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

We refer to [these lectures](https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/pages/video-lectures-and-slides/fixed-income-securities/).

--- 

Treasury Bonds are debt securities issued by the government to finance its operations. They are known for their stability and are key instruments in the financial markets. Below is a structured explanation of the key concepts related to Treasury Bonds.


### **1. Intrinsic Properties of Treasury Bonds**
Treasury Bonds have two intrinsic properties:
- **Face Value (Principal):**  
  The amount paid to the bondholder at maturity. Typically, the face value is $1,000, though this may vary.
  
- **Coupon Rate:**  
  The fixed annual interest rate set at the time of issuance, expressed as a percentage of the face value.  
  - **Example:** A bond with a face value of $1,000 and a coupon rate of 5% will pay $50 in interest annually.


### **2. How Treasury Bonds Work**
When you hold a Treasury Bond, you receive:
1. **Periodic Coupon Payments:** These payments are based on the bond's coupon rate. Payments are typically made semi-annually.  
2. **Face Value at Maturity:** At the end of the bond's term, the face value is returned to the holder.

#### **Illustration: Bond Payment Timeline**
```
|--------------------|--------------------|--------------------| Maturity
$25                 $25                 $25                 $1,000
(Coupon Payment)   (Coupon Payment)   (Coupon Payment)   (Face Value + Coupon Payment)
```

---

### **3. Market Trading: Price and Yield**
Treasury Bonds are traded in the secondary market, and their **price** and **yield** vary based on market conditions.

- **Price:** The price of a bond is what investors are willing to pay for it. It may differ from the face value due to changes in interest rates and demand.  
  - If market interest rates fall below the bond's coupon rate, the bond price rises (a premium).  
  - If market interest rates rise above the bond's coupon rate, the bond price falls (a discount).

- **Yield:** The return an investor earns if they buy the bond at the current price and hold it until maturity.  
  - **Inverse Relationship:** Price and yield move in opposite directions. When the bond price goes up, the yield goes down, and vice versa.


### **4. Calculating Bond Price and Yield to Maturity**
The **price of a bond** is calculated as the present value of all future cash flows (coupon payments and face value) discounted by the yield to maturity (YTM).  
### Formula:
\[
P = \sum \frac{C}{(1 + YTM)^t} + \frac{F}{(1 + YTM)^T}
\]
Where:  
- \(P\): Price of the bond  
- \(C\): Coupon payment  
- \(F\): Face value  
- \(t\): Each payment period  
- \(T\): Total number of periods  

#### **Illustration: Bond Pricing**
Consider a bond with:  
- Face Value (\(F\)) = $1,000  
- Coupon Payment (\(C\)) = $50 (5% annual coupon rate, paid semi-annually)  
- Yield to Maturity (YTM) = 4% (annualized)  
- Maturity = 10 years (20 semi-annual periods)

Using the formula, you calculate the present value of all cash flows to determine the price.


### **5. Interest Rates and Bond Prices**
- Bond prices are influenced by **interest rate expectations**. When market participants anticipate future interest rate changes, they adjust bond prices accordingly.  
- **Future Predictions:** Because bond prices reflect expected interest rates, they serve as indicators of long-term interest rate trends.


### **6. Spot Rate vs. Yield to Maturity**
- **Spot Rate:** The yield for a specific period in the future. It applies to zero-coupon bonds, where no intermediate payments are made.  
- **Yield to Maturity (YTM):** The average annual return if the bond is held to maturity, considering all future cash flows.


### **7. Treasury Bonds as Predictors of Economic Trends**
Treasury Bonds are closely watched because their yields provide insights into investor expectations about the economy. The **yield curve**, which plots the yield of bonds against their maturity, is a key tool for this purpose.

#### **a. Normal Yield Curve (Positive Slope)**  
- **Definition:** In a normal yield curve, long-term yields are higher than short-term yields.  
- **Reason:** Investors demand a higher return for lending money over longer periods to compensate for risks such as inflation and uncertainty.  
- **Economic Signal:** Indicates a healthy, growing economy.  

**Example:**  
- 2-year Treasury yield: 2.5%  
- 10-year Treasury yield: 3.5%  
- 30-year Treasury yield: 4.0%  

**Illustration:**  
```
Yield (%)
|
|       *
|     *   
|   *     
| *        
|___________________
  1Y   5Y   10Y  30Y
       Maturity
```

**Interpretation:**  
Investors expect stable growth, and the higher yields on long-term bonds reflect a normal expectation of risk and inflation over time.

#### **b. Inverted Yield Curve (Negative Slope)**  
- **Definition:** In an inverted yield curve, short-term yields are higher than long-term yields.  
- **Reason:** Investors expect economic slowdowns or recessions, causing them to shift money into long-term bonds for safety. This increased demand for long-term bonds lowers their yield.  
- **Economic Signal:** Often a precursor to a recession. Historically, an inverted curve has predicted recessions in the U.S. with high accuracy.  

**Example:**  
- 2-year Treasury yield: 4.5%  
- 10-year Treasury yield: 3.0%  
- 30-year Treasury yield: 2.5%  

**Illustration:**  
```
Yield (%)
|
| *        
|   *      
|     *    
|       *  
|___________________
  1Y   5Y   10Y  30Y
       Maturity
```

**Interpretation:**  
Investors expect the economy to weaken in the near term, reducing inflation and interest rates over time.


