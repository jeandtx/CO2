def load_clean_data():
    import numpy as np
    import pandas as pd
    carbone = pd.read_csv('./pages/carbone.csv')
    carbone.drop([
        "Statut de l'élément", 'Code gaz supplémentaire 2', 'Valeur gaz supplémentaire 2',
        'Code gaz supplémentaire 3', 'Valeur gaz supplémentaire 3',
        'Code gaz supplémentaire 4', 'Valeur gaz supplémentaire 4',
        'Code gaz supplémentaire 5', 'Valeur gaz supplémentaire 5'], axis=1, inplace=True)
    return carbone


def load_dataset():
    import numpy as np
    import pandas as pd
    carbone = pd.read_csv('./pages/carbone.csv')
    return carbone


def load_industry():
    import numpy as np
    import pandas as pd
    industry = pd.read_csv('./pages/industry.csv')
    return industry
