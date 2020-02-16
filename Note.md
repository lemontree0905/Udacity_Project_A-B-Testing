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
    - P_{pool}=\frac{X_{cont}+X_{exp}}{N_{cont}+N_{exp}}
    SE_{pool}=\sqrt{P_{pool}(1-P_{pool})(\frac{1}{N_{cont}}+\frac{1}{N_{exp}})}
    
- Practically Significant (Substantive) & Statistically Significant
