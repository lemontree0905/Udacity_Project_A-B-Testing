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
 
## Lesson 2 Policy and Ethics for Experiments
Four Principles of IRB's (Institutional Research Boards): Risk, Benefits, Alternatives, Data Sensitivity


## Lesson3 Choosing and Characterizing Metrics
### Metric Definition Overview
- Invariant checking (Sanity check) & Evaluation
- Highlevel concepts for metrics
- Difficult metrics
  - Don't have access to data
  - Takes too long
- Other Techniques
  - External Data
  - Retrospective or observational analysis (establish **correlation** not **causation**)
  - Gathering Your Own In-Depth Data
    - User Experience Research (UER): 
    - Focus groups
    - Surveys
###  Metric Definition
- Click-through-probability = Unique visitors who click/Unique visitors to page
  - How to define a unique visitor (cookie, unique id for each page view)
  - Time period
  
### Filtering and Segmenting

### Summary metrics
- Categories
  - Sum and counts
  - Distributional metrics: means, median, percentiles
  - Probabilities and Rates
  - Ratios
  
### Sensitivity and Robustness

### Variability 
|type of metric |distribution| estimated variance
| --- | --- | --- |
|probability | binomial | p(1-p)/N
|mean |	Normal | sigma^2/N
|median/percentile| depends | depends
| counts/difference | normal(maybe)| Var(X)+Var(Y)
| rates | poisson | \bar{x}
| ratios| depends | depends

## Lesson4 Designing an Experiment
### Choose 'subject'
- unit of division
  - user id: stable, unchanging
  - anonymous id (cookie): change when you switch browser or device, user can clear cookie
  - Event: no consistent experience
  - Device id: only availabe for mobile
  - IP address
- Consistency of Diversion
  - user consistency
  - Ethical considerations
  - Unit of Analysis vs Unit of Diversion
### Choose 'population'
- Inter- vs. Intra-User Experiments
- Target Population
- Cohort: Enter the experiment around the same time
  - Anything require **user stability**
  - looking for learning effects
  - examing user retention
  - increase user activity
### Experiment Design and Sizing
### Duration vs. Exposure

## Lesson5 Analyzing Results
### Multiple Metric
- False positive
  - Assuming independent  
    \alpha_{overall} = 1 - (1-\alpha)^n
  - Bonferroni correction (no assumption,conservative)  
    \alpha = \alpha_{overall} / n
    
