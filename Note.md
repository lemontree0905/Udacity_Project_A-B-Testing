# A/B Testing

## Lesson 1 Overview of A/B Testing

### A/B tesing not useful for new experience
- change aversion & novelty effect
- What's your baseline for comparison & How much time you need

### Metric Choice
- To measure the usability: Click-through-rate(CTR) = Number of clicks/Number of page views
- To measure the total impact: Click-through-probability = Unique visitors who click/Unique visitors to page

### Review Statistics
- Calculate a confidence interval
  - To use normal : Np>5 and N(1-p)>5
  - Pooled Standard Error 
    <p align="center"><a href="https://www.codecogs.com/eqnedit.php?latex=P_{pool}=\frac{X_{cont}&plus;X_{exp}}{N_{cont}&plus;N_{exp}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P_{pool}=\frac{X_{cont}&plus;X_{exp}}{N_{cont}&plus;N_{exp}}" title="P_{pool}=\frac{X_{cont}+X_{exp}}{N_{cont}+N_{exp}}" /></a></p>
     <p align="center"><a href="https://www.codecogs.com/eqnedit.php?latex=SE_{pool}=\sqrt{P_{pool}(1-P_{pool})(\frac{1}{N_{cont}}&plus;\frac{1}{N_{exp}})}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?SE_{pool}=\sqrt{P_{pool}(1-P_{pool})(\frac{1}{N_{cont}}&plus;\frac{1}{N_{exp}})}" title="SE_{pool}=\sqrt{P_{pool}(1-P_{pool})(\frac{1}{N_{cont}}+\frac{1}{N_{exp}})}" /></a></p>
        
- Practicall Significance (Substantive) & Statistical Significance

### Design
- Size vs. Power trade-off
  - Significance level alpha: alpha = P(reject null|null true)
  - Sensitivity 1-beta: beta = P(fail to reject|null false) 
    http://www.evanmiller.org/ab-testing/sample-size.html
    
### Analyze
- Confidence Interval Cases
 
