import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Hrishi99',
    'database': 'digidine',
}


def execute_procedure(procedure_name):
    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Call the stored procedure
        cursor.callproc(procedure_name)

        # Fetch the result set
        result = list(cursor.stored_results())[0].fetchall()

        return result

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the database connection
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

def plot_user_dietary_restrictions(result):
    df = pd.DataFrame(result, columns=['Diet', 'Count'])
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Diet', y='Count', data=df)
    plt.title('User Dietary Restrictions')
    plt.xlabel('Diet')
    plt.ylabel('Count')
    plt.show()

def plot_ingredient_distribution(result):
    df = pd.DataFrame(result, columns=['Ingredient', 'Count'])
    plt.figure(figsize=(12, 8))
    sns.barplot(x='Ingredient', y='Count', data=df)
    plt.title('Ingredient Distribution in Fridges')
    plt.xlabel('Ingredient')
    plt.ylabel('Count')
    plt.show()

def plot_user_flavour_preferences(result):
    df = pd.DataFrame(result, columns=['User', 'Flavour'])
    plt.figure(figsize=(12, 8))
    sns.countplot(x='Flavour', data=df, hue='User')
    plt.title('User Flavour Preferences')
    plt.xlabel('Flavour')
    plt.ylabel('Count')
    plt.show()


def plot_user_fridge_color_distribution(result):
    df = pd.DataFrame(result, columns=['User', 'Fridge Color'])
    plt.figure(figsize=(10, 8))
    sns.countplot(x='Fridge Color', data=df, hue='User')
    plt.title('User Fridge Color Distribution')
    plt.xlabel('Fridge Color')
    plt.ylabel('Count')
    plt.show()

def plot_recipe_flavour_distribution(result):
    df = pd.DataFrame(result, columns=['Recipe', 'Flavour'])
    plt.figure(figsize=(12, 8))
    sns.countplot(x='Flavour', data=df, hue='Recipe')
    plt.title('Recipe Flavour Distribution')
    plt.xlabel('Flavour')
    plt.ylabel('Count')
    plt.show()

def plot_user_ingredient_preferences(result):
    df = pd.DataFrame(result, columns=['User', 'Ingredient'])
    pivot_table = df.pivot_table(index='User', columns='Ingredient', aggfunc='size').fillna(0)
    if pivot_table.empty:
        print("No data to plot.")
        return
    plt.figure(figsize=(14, 10))
    sns.heatmap(pivot_table, cmap='viridis', cbar=False)
    plt.title('User Ingredient Preferences')
    plt.xlabel('Ingredient')
    plt.ylabel('User')
    plt.show()


def plot_ingredient_dietary_restrictions(result):
    df = pd.DataFrame(result, columns=['Ingredient', 'Dietary Restriction'])
    plt.figure(figsize=(12, 8))
    sns.countplot(x='Dietary Restriction', data=df, hue='Ingredient')
    plt.title('Ingredient Dietary Restrictions')
    plt.xlabel('Dietary Restriction')
    plt.ylabel('Count')
    plt.show()

def plot_chef_recipe_count(result):
    df = pd.DataFrame(result, columns=['Chef', 'Recipe Count'])
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Chef', y='Recipe Count', data=df)
    plt.title('Chef Recipe Count')
    plt.xlabel('Chef')
    plt.ylabel('Recipe Count')
    plt.show()

def plot_user_ingredient_caloric_intake(result):
    df = pd.DataFrame(result, columns=['User', 'Ingredient', 'Calories'])
    plt.figure(figsize=(12, 8))
    sns.scatterplot(x='Calories', y='User', data=df)
    plt.title('User Ingredient Caloric Intake')
    plt.xlabel('Calories')
    plt.ylabel('User')
    plt.show()

def plot_user_ingredient_preferences_heatmap(result):
    df = pd.DataFrame(result, columns=['User', 'Ingredient'])

    pivot_table = df.pivot_table(index='User', columns='Ingredient', aggfunc='size').fillna(0)

    if pivot_table.empty:
        print("No data to plot.")
        return
    plt.figure(figsize=(14, 10))
    sns.heatmap(pivot_table, cmap='viridis', cbar=True, cbar_kws={'label': 'Count'})
    plt.title('User Ingredient Preferences Heatmap')
    plt.xlabel('Ingredient')
    plt.ylabel('User')
    plt.show()



# Call the procedures and visualize the results
user_dietary_restrictions_result = execute_procedure('GetUserDietaryRestrictions')
plot_user_dietary_restrictions(user_dietary_restrictions_result)

ingredient_distribution_result = execute_procedure('GetIngredientDistributionInFridges')
plot_ingredient_distribution(ingredient_distribution_result)

user_flavour_preferences_result = execute_procedure('GetUserFlavourPreferences')
plot_user_flavour_preferences(user_flavour_preferences_result)

user_fridge_color_distribution_result = execute_procedure('GetUserFridgeColorDistribution')
plot_user_fridge_color_distribution(user_fridge_color_distribution_result)

recipe_flavour_distribution_result = execute_procedure('GetRecipeFlavourDistribution')
plot_recipe_flavour_distribution(recipe_flavour_distribution_result)

user_ingredient_preferences_result = execute_procedure('GetUserIngredientPreferences')
plot_user_ingredient_preferences(user_ingredient_preferences_result)

ingredient_dietary_restrictions_result = execute_procedure('GetIngredientDietaryRestrictions')
plot_ingredient_dietary_restrictions(ingredient_dietary_restrictions_result)

chef_recipe_count_result = execute_procedure('GetChefRecipeCount')
plot_chef_recipe_count(chef_recipe_count_result)

user_ingredient_caloric_intake_result = execute_procedure('GetUserIngredientCaloricIntake')
plot_user_ingredient_caloric_intake(user_ingredient_caloric_intake_result)

user_ingredient_preferences_heatmap_result = execute_procedure('GetUserIngredientPreferencesHeatmap')
plot_user_ingredient_preferences_heatmap(user_ingredient_preferences_heatmap_result)
