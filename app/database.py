from bson.objectid import ObjectId
import pandas as pd
import math

data_folder = 'app/static/'
age_equivalence = pd.read_csv(data_folder + 'age_equivalence.csv', header=[0])
vmi = pd.read_csv(data_folder + '1_natural_vmi_to_standard.csv', header=[0,1])
visual = pd.read_csv(data_folder + '2_natural_visual_to_standard.csv', header=[0,1])
motor = pd.read_csv(data_folder + '3_natural_motor_to_standard.csv', header=[0,1])
percentiles =  pd.read_csv(data_folder + 'standard_to_percentiles.csv', header=[0])
performance =  pd.read_csv(data_folder + 'performance_from_estandar.csv', header=[0])

def get_standard_score(df, natural, age_years, age_months):
    natural_values = df.natural.set_axis(['natural'], axis=1, inplace=False)
    values_by_years = df[str(age_years)]
    df= pd.concat([natural_values, values_by_years], axis=1)
    natural_row = df[df.natural == natural]
    for column in df.columns[1:]:
        months = column.split('-')
        months = list(map(int, months))
        if months[0] <= age_months <= months[1]:
            selected_column = column
    standard_value = natural_row[selected_column].values[0]
    if (math.isnan(standard_value)): standard_value = '-'
    return standard_value

def get_age_equivalence(df, natural, value_name):
    age_equivalence = df[df.natural == natural][value_name].values[0]
    try:
        age_equivalence = age_equivalence.split('-')
    except:
        age_equivalence = '-'
    return age_equivalence

def get_scaled_values(df, standard):    
    try:
        scaled_value = df[df.standard == standard]['scaled'].values[0]
    except:
        scaled_value = '-'
    return scaled_value

def get_percentile_values(df, standard):
    try:
        percentile = df[df.standard == standard]['percentiles'].values[0]
    except:
        percentile = '-'
    return percentile

def get_performance_level(df, standard):
    try:
        standard = int(standard)
        for i, standard_interval in enumerate(df.standard):
            values = standard_interval.split('-')
            if (standard >= int(values[0]) and standard <= int(values[1])):
                return(df.performance.values[i])
    except:
        return '-'

def vmi_helper(vmi) -> dict:
    return {
        "standard_scores": vmi["standard_scores"],
        "scaled_scores": vmi["scaled_scores"],
        "percentiles": vmi["percentiles"],
        "age_equivalences": vmi["age_equivalences"],
        "performances": vmi["performances"]
    }

async def get_vmi_report(id: str, age_years: int, age_months: int, vmi_natural_score: int, visual_natural_score: int, motor_natural_score: int) -> dict:
    standard_vmi = get_standard_score(vmi, vmi_natural_score, age_years, age_months)
    standard_visual = get_standard_score(visual, visual_natural_score, age_years, age_months)
    standard_motor = get_standard_score(motor, motor_natural_score, age_years, age_months)
    
    standard_scores = {
        'vmi': standard_vmi,
        'visual': standard_visual,
        'motor': standard_motor,
    }
    scaled_vmi = get_scaled_values(percentiles, standard_vmi)
    scaled_visual = get_scaled_values(percentiles, standard_visual)
    scaled_motor = get_scaled_values(percentiles, standard_motor)
    
    scaled_scores = {
        'vmi': scaled_vmi,
        'visual': scaled_visual,
        'motor': scaled_motor,
    }

    percentile_vmi = get_percentile_values(percentiles, standard_vmi)
    percentile_visual = get_percentile_values(percentiles, standard_visual)
    percentile_motor = get_percentile_values(percentiles, standard_motor)
    
    percentile_values = {
        'vmi': percentile_vmi,
        'visual': percentile_visual,
        'motor': percentile_motor,
    }

    vmi_age = get_age_equivalence(age_equivalence, vmi_natural_score, 'vmi')
    visual_age = get_age_equivalence(age_equivalence, visual_natural_score, 'visual')
    motor_age = get_age_equivalence(age_equivalence, motor_natural_score, 'motor')

    age_equivalences = {
        'vmi': vmi_age,
        'visual': visual_age,
        'motor': motor_age,
    }

    vmi_performance = get_performance_level(performance, standard_vmi)
    visual_performance = get_performance_level(performance, standard_visual)
    motor_performance = get_performance_level(performance, standard_motor)

    performances = {
        'vmi': vmi_performance,
        'visual': visual_performance,
        'motor': motor_performance,
    }

    vmi_result = {
        "standard_scores": standard_scores,
        "scaled_scores": scaled_scores,  
        "percentiles": percentile_values,
        "age_equivalences": age_equivalences,
        "performances": performances
    }

    return vmi_helper(vmi_result)