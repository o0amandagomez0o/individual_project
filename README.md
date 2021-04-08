<div style="text-align:center"><img src="https://i.pinimg.com/originals/97/1b/e6/971be6140958f13c4a85145e64f968ec.png"/></div>

___

<a id='navigation'></a>


[[Project Planning](#project-planning)]
[[Key Findings](#key-findings)]
[[Tested Hypotheses](#tested-hypotheses)]
[[Take Aways](#take-aways)]
[[Data Dictionary](#data-dictionary)]
[[Workflow](#workflow)]

___



<a name="project-planning"></a><h1><img src="https://i.pinimg.com/originals/08/5a/eb/085aeb8e6c5addd4114c7ecc12166145.png"/></h1>

### Goal: 
The goal for this project is to create a model that will accurately predict the likelihood of a pet getting adopted from Austin Animal Center.

### Initial Hypotheses:

> Hypothesis₁
>
> There is a relationship between age and adoption.
    
> Hypothesis₂
>
> There is a relationship between breed and adoption.
    
> Hypothesis₃
>
> Dogs are adopted more than cats.
    
> Hypothesis₄
>
> There is a relationship between color and adoption.
    
### Project Planning Initial Thoughts:
**First iteration:**
I'd like my first iteration to include as many encoded features as possible for cats and dogs only. 

**Second iteration:**
I'd like to use takeaways from my exploration to cluster some features and use feature importance to remove features that aren't helping my model. 
- Cluster: 
- New features:
    - age range/bin
    - encode animal type
    - binary encoded column of adoption
    - encode sex
        - include a feature of spayed/neutered
    - 

**Deliverables:**
- Final clean, interactive Py notebook.
- README.md
- Project summary
    
    
[Jump to Navigation](#navigation)

<a name="key-findings"></a><h1><img src="https://i.pinimg.com/originals/82/02/e8/8202e8d3a1cfda0a8d828ea688b6b36e.png"/></h1>

## Exploration Key Findings:

- Ventura is a quarter of LA and OC is half of LA
- Lot size is thrown off by outliers
- home_value median price is $ 355_758
- land_value has a similar distribution to home_value, but priced lesser
- home_age is almost normally distributed.

The following features appear to have clusters to explore:

- home_age & home_value
- home_age & sqft
- lot_sqft & sqft
- home_value & sqft
- longitude & property_quality
- home_age & property_quality


[Jump to Navigation](#navigation)

<a name="tested-hypotheses"></a><h1><img src="https://i.pinimg.com/originals/f8/6c/1f/f86c1fc26068ad184455e11c7c5858cc.png"/></h1>


> Hypothesis₁
>
> H₀ = No correlation between `home_age` and `logerror`.
>
> H𝛼 = There IS a correlation between `home_age` and `logerror`.
> - REJECT null hypothesis.

<details>
  <summary>Click to see full list. </summary>
    
> Hypothesis₂
>
> H₀ = No correlation between `lot_sqft` and `logerror`.
>
> H𝛼 = There IS a correlation between `lot_sqft` and `logerror`.
> - FAIL to reject null hypothesis.
    
       
> Hypothesis₃
>
> H₀ = No correlation between `home_value` and `logerror`.
>
> H𝛼 = There IS a correlation between `home_value` and `logerror`.
> - FAIL to reject null hypothesis.    
   
    
> Hypothesis₄
>
> H₀ = Mean logerror is the same for small homes on small lots & Average sized homes on small lots.
>
> H𝛼 = Mean logerror for small homes on small lots & Average sized homes on small lots are different.
> - FAIL to reject null hypothesis.
  
    
> Hypothesis₅
>
> H₀ = Mean logerror is the same for properties in Los Angeles County & Orange County.
>
> H𝛼 = Mean logerror for properties in Los Angeles County & Orange County are different.
> - REJECT null hypothesis.
    
> Hypothesis₆
>
> H₀ = Mean logerror is the same for properties in Los Angeles County & Ventura County.
>
> H𝛼 = Mean logerror for properties in Los Angeles County & Ventura County are different.
> - FAIL to reject null hypothesis.
    
> Hypothesis₇
>
> H₀ = Mean logerror is the same for properties in Orange County & Ventura County.
>
> H𝛼 = Mean logerror for properties in Orange County & Ventura County are different.
> - FAIL to reject null hypothesis.
    
    
</details>


    
[Jump to Navigation](#navigation)

<a name="take-aways"></a><h1><img src="https://i.pinimg.com/originals/0b/24/91/0b2491f3c35b30155defee2f5ee6c3c3.png"/></h1>

> - `home_age` and `logerror` had a weak linear relationship, at best
>
> - `lot_sqft` did not have a significant effect on `logerror`, which we found surprising
>
> - also surprising was the apparent lack of significance between `home_value` and `logerror`

- Out of our homemade features, small homes of all ages , large homes, and homes that are considered "best quality" seem to be drivers of logerror.


[Jump to Navigation](#navigation)

<a name="data-dictionary"></a><h1><img src="https://i.pinimg.com/originals/2f/d4/c1/2fd4c1a67997f7c7c32b556aefd7ce1a.png"/></h1>

| column_name                 | description                                                                                                         | key             | dtype    |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------|-----------------|----------|
| `parcelid`                  | Unique identifier for parcels (lots)                                                                                |                 | int64    |


<details>
  <summary>Click to see full list. </summary>

| column_name                 | description                                                                                                         | key             | dtype    |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------|-----------------|----------| 
| `young_smhome`              | Indicates if the property is a young small square footage home.                                                     | 1 = yes, 0 = no | uint8    |

        
</details>

[Jump to Navigation](#navigation)

<a name="workflow"></a><h1><img src="https://i.pinimg.com/originals/96/13/36/961336fdcedb8a6025a978410e0d14b3.png"/></h1>

    




[Jump to Navigation](#navigation)












































