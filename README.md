<div style="text-align:center"><img src="https://i.pinimg.com/originals/97/1b/e6/971be6140958f13c4a85145e64f968ec.png"/></div>

___

<a id='navigation'></a>


[[Project Planning](#project-planning)]
[[Key Findings](#key-findings)]
[[Tested Hypotheses](#tested-hypotheses)]
[[Take Aways](#take-aways)]
[[Data Dictionary](#data-dictionary)]
[[Repo Replication](#repo-replication)]

___



<a name="project-planning"></a><h1><img src="https://i.pinimg.com/originals/9f/b7/6d/9fb76d0350228675d02435d4f5aa1197.png"/></h1>
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

<a name="key-findings"></a><h1><img src="https://i.pinimg.com/originals/3a/1e/6d/3a1e6d338b1b0bd1850f2eb067f983b4.png"/></h1>

## Exploration Key Findings:




[Jump to Navigation](#navigation)

<a name="tested-hypotheses"></a><h1><img src="https://i.pinimg.com/originals/35/3f/e6/353fe67133773dc3639f95987d57c386.png"/></h1>


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

<a name="take-aways"></a><h1><img src="https://i.pinimg.com/originals/3f/d3/66/3fd3660db4a243c2e43640a28a44d4c2.png"/></h1>




[Jump to Navigation](#navigation)

<a name="data-dictionary"></a><h1><img src="https://i.pinimg.com/originals/3f/84/53/3f8453f4d3e1ff56d3934dd6ebe1d410.png"/></h1>

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

<a name="repo-replication"></a><h1><img src="https://i.pinimg.com/originals/d5/24/a6/d524a6bb62a9d6734c7cf899a11c7310.png"/></h1>

    




[Jump to Navigation](#navigation)












































