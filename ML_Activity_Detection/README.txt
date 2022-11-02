"""
Select the model
"""
modelList = [] 

# Select from the list of model in the pipeline/models folder
for x in os.listdir("./pipeline/models"): 
    modelList += [x]

# Widgets
confirmButton = widgets.Button(
    description='Confirm',
    disabled=False,
    button_style='success',
    icon='check'
)
modelDropdown = widgets.Dropdown(
    options=modelList,
    value=modelList[0],
    description='Model:')
# Function on what happen when confirm is been click.
def selectWidgetSet(b):
    print("Selected: " , modelDropdown.value)

confirmButton.on_click(selectWidgetSet)
modelBox = widgets.VBox([widgets.HBox([modelDropdown, confirmButton])])
modelBox