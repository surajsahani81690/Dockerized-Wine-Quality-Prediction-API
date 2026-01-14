from pydantic import BaseModel, Field
from typing import Annotated

class UserInput(BaseModel):
    fixed_acidity: Annotated[
        float, Field(..., description="Fixed acidity of the wine")
    ]
    volatile_acidity: Annotated[
        float, Field(..., description="Volatile acidity of the wine")
    ]
    citric_acid: Annotated[
        float, Field(..., description="Citric acid content of the wine")
    ]
    residual_sugar: Annotated[
        float, Field(..., description="Residual sugar in the wine")
    ]
    chlorides: Annotated[
        float, Field(..., description="Chlorides content of the wine")
    ]
    free_sulfur_dioxide: Annotated[
        float, Field(..., description="Free sulfur dioxide in the wine")
    ]
    total_sulfur_dioxide: Annotated[
        float, Field(..., description="Total sulfur dioxide in the wine")
    ]
    density: Annotated[
        float, Field(..., description="Density of the wine")
    ]
    pH: Annotated[
        float, Field(..., description="pH level of the wine")
    ]
    sulphates: Annotated[
        float, Field(..., description="Sulphates content of the wine")
    ]
    alcohol: Annotated[
        float, Field(..., description="Alcohol percentage of the wine")
    ]
