import wandb
import random
import math
import csv


# Start a new run
run = wandb.init(project='custom-charts')
offset = random.random()



# At each time step in the model training loop
for run_step in range(20):

  # Log basic experiment metrics, which show up as standard line plots in the UI
  wandb.log({
      "loss": math.log(1 + random.random() + run_step) + offset,
      "val_acc": math.log(1 + random.random() + run_step) + offset * random.random(),
  }, commit=False)

  # Set up data to log in custom charts
  data1 = open('/content/drive/MyDrive/Colab/ICT3104/testing_data/visualise.csv')

  type(data1)
  csvreader = csv.reader(data1)
  header = []
  header = next(csvreader)
  rows = []

  for row in csvreader:
    rows.append(row)

  data = []
  for i in range(len(rows)):
    data.append([i, rows[i]])
  
  # Create a table with the columns to plot
  table = wandb.Table(data=rows, columns=["loss", "accuracy"])

  # Use the table to populate various custom charts
  line_plot = wandb.plot.line(table, x='loss', y='accuracy', title='Line Plot')
  histogram = wandb.plot.histogram(table, value='accuracy', title='Histogram')
  scatter = wandb.plot.scatter(table, x='loss', y='accuracy', title='Scatter Plot')
  
  # Log custom tables, which will show up in customizable charts in the UI
  wandb.log({'line_1': line_plot, 
             'histogram_1': histogram, 
             'scatter_1': scatter})

# Finally, end the run. We only need this ine in Jupyter notebooks.
run.finish()