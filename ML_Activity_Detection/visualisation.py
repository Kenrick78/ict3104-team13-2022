import wandb

wandb.init(project="my-test-project")

wandb.config = {
  "learning_rate": 0.001,
  "epochs": 100,
  "batch_size": 128
}
