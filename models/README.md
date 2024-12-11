# Training Result

## SingleTransferRoBERTa

### 100p
```
=== train SingleTransferRoBERTa - 100p ===
  checkpoint = torch.load(model_path)
No checkpoint found. Starting training from scratch...
Training Epoch 1/10: 100% 254/254 [04:54<00:00,  1.16s/it]
Validation: 100% 29/29 [00:10<00:00,  2.68it/s]
Epoch 1/10, Train Loss: 0.6592, Validation Loss: 0.2092, Accuracy: 94.56%
Training Epoch 2/10: 100% 254/254 [04:53<00:00,  1.16s/it]
Validation: 100% 29/29 [00:10<00:00,  2.68it/s]
Epoch 2/10, Train Loss: 0.1561, Validation Loss: 0.1345, Accuracy: 96.11%
Training Epoch 3/10: 100% 254/254 [04:53<00:00,  1.16s/it]
Validation: 100% 29/29 [00:10<00:00,  2.69it/s]
Epoch 3/10, Train Loss: 0.1062, Validation Loss: 0.1180, Accuracy: 96.33%
Training Epoch 4/10: 100% 254/254 [04:53<00:00,  1.16s/it]
Validation: 100% 29/29 [00:10<00:00,  2.69it/s]
Epoch 4/10, Train Loss: 0.0852, Validation Loss: 0.1248, Accuracy: 96.22%
Training Epoch 5/10: 100% 254/254 [04:53<00:00,  1.16s/it]
Validation: 100% 29/29 [00:10<00:00,  2.69it/s]
Epoch 5/10, Train Loss: 0.0725, Validation Loss: 0.1082, Accuracy: 96.17%
Training Epoch 6/10: 100% 254/254 [04:53<00:00,  1.16s/it]
Validation: 100% 29/29 [00:10<00:00,  2.69it/s]
Epoch 6/10, Train Loss: 0.0663, Validation Loss: 0.1032, Accuracy: 96.56%
Training Epoch 7/10: 100% 254/254 [04:53<00:00,  1.16s/it]
Validation: 100% 29/29 [00:10<00:00,  2.68it/s]
Epoch 7/10, Train Loss: 0.0644, Validation Loss: 0.0980, Accuracy: 97.11%
Training Epoch 8/10: 100% 254/254 [04:53<00:00,  1.16s/it]
Validation: 100% 29/29 [00:10<00:00,  2.68it/s]
Epoch 8/10, Train Loss: 0.0636, Validation Loss: 0.1122, Accuracy: 96.61%
Training Epoch 9/10: 100% 254/254 [04:53<00:00,  1.16s/it]
Validation: 100% 29/29 [00:10<00:00,  2.69it/s]
Epoch 9/10, Train Loss: 0.0488, Validation Loss: 0.1096, Accuracy: 96.56%
Training Epoch 10/10: 100% 254/254 [04:53<00:00,  1.16s/it]
Validation: 100% 29/29 [00:10<00:00,  2.69it/s]
Epoch 10/10, Train Loss: 0.0518, Validation Loss: 0.1074, Accuracy: 96.67%
Early stopping triggered after epoch 10
=== SingleTransferRoBERTa - 100p training completed ===
```

### 10p
```
=== train SingleTransferRoBERTa - 10p ===
  checkpoint = torch.load(model_path)
No checkpoint found. Starting training from scratch...
Training Epoch 1/10: 100% 26/26 [00:29<00:00,  1.13s/it]
Validation: 100% 3/3 [00:01<00:00,  2.76it/s]
Epoch 1/10, Train Loss: 1.8027, Validation Loss: 1.7720, Accuracy: 26.11%
Training Epoch 2/10: 100% 26/26 [00:29<00:00,  1.13s/it]
Validation: 100% 3/3 [00:01<00:00,  2.76it/s]
Epoch 2/10, Train Loss: 1.3514, Validation Loss: 0.8059, Accuracy: 72.22%
Training Epoch 3/10: 100% 26/26 [00:29<00:00,  1.13s/it]
Validation: 100% 3/3 [00:01<00:00,  2.77it/s]
Epoch 3/10, Train Loss: 0.5660, Validation Loss: 0.4332, Accuracy: 82.78%
Training Epoch 4/10: 100% 26/26 [00:29<00:00,  1.13s/it]
Validation: 100% 3/3 [00:01<00:00,  2.77it/s]
Epoch 4/10, Train Loss: 0.2991, Validation Loss: 0.4211, Accuracy: 85.00%
Training Epoch 5/10: 100% 26/26 [00:29<00:00,  1.13s/it]
Validation: 100% 3/3 [00:01<00:00,  2.78it/s]
Epoch 5/10, Train Loss: 0.1734, Validation Loss: 0.3355, Accuracy: 88.89%
Training Epoch 6/10: 100% 26/26 [00:29<00:00,  1.13s/it]
Validation: 100% 3/3 [00:01<00:00,  2.77it/s]
Epoch 6/10, Train Loss: 0.0930, Validation Loss: 0.3598, Accuracy: 89.44%
Training Epoch 7/10: 100% 26/26 [00:29<00:00,  1.13s/it]
Validation: 100% 3/3 [00:01<00:00,  2.77it/s]
Epoch 7/10, Train Loss: 0.0718, Validation Loss: 0.4548, Accuracy: 89.44%
Training Epoch 8/10: 100% 26/26 [00:29<00:00,  1.13s/it]
Validation: 100% 3/3 [00:01<00:00,  2.77it/s]
Epoch 8/10, Train Loss: 0.0584, Validation Loss: 0.5356, Accuracy: 85.00%
Early stopping triggered after epoch 8
=== SingleTransferRoBERTa - 10p training completed ===
```

### 1p
```
=== train SingleTransferRoBERTa - 1p ===
  checkpoint = torch.load(model_path)
No checkpoint found. Starting training from scratch...
Training Epoch 1/10: 100% 3/3 [00:02<00:00,  1.01it/s]
Validation: 100% 1/1 [00:00<00:00,  9.06it/s]
Epoch 1/10, Train Loss: 1.8594, Validation Loss: 1.7965, Accuracy: 16.67%
Training Epoch 2/10: 100% 3/3 [00:03<00:00,  1.00s/it]
Validation: 100% 1/1 [00:00<00:00,  8.96it/s]
Epoch 2/10, Train Loss: 1.8129, Validation Loss: 1.7946, Accuracy: 16.67%
Training Epoch 3/10: 100% 3/3 [00:03<00:00,  1.00s/it]
Validation: 100% 1/1 [00:00<00:00,  9.00it/s]
Epoch 3/10, Train Loss: 1.7931, Validation Loss: 1.7922, Accuracy: 16.67%
Training Epoch 4/10: 100% 3/3 [00:02<00:00,  1.00it/s]
Validation: 100% 1/1 [00:00<00:00,  9.08it/s]
Epoch 4/10, Train Loss: 1.7780, Validation Loss: 1.7903, Accuracy: 22.22%
Training Epoch 5/10: 100% 3/3 [00:03<00:00,  1.00s/it]
Validation: 100% 1/1 [00:00<00:00,  9.08it/s]
Epoch 5/10, Train Loss: 1.7651, Validation Loss: 1.7900, Accuracy: 16.67%
Training Epoch 6/10: 100% 3/3 [00:02<00:00,  1.01it/s]
Validation: 100% 1/1 [00:00<00:00,  9.07it/s]
Epoch 6/10, Train Loss: 1.7404, Validation Loss: 1.7913, Accuracy: 22.22%
Training Epoch 7/10: 100% 3/3 [00:02<00:00,  1.02it/s]
Validation: 100% 1/1 [00:00<00:00,  9.10it/s]
Epoch 7/10, Train Loss: 1.7110, Validation Loss: 1.8008, Accuracy: 22.22%
Training Epoch 8/10: 100% 3/3 [00:02<00:00,  1.02it/s]
Validation: 100% 1/1 [00:00<00:00,  9.01it/s]
Epoch 8/10, Train Loss: 1.5907, Validation Loss: 1.8340, Accuracy: 33.33%
Early stopping triggered after epoch 8
=== SingleTransferRoBERTa - 1p training completed ===
```

## SingleTransferBERT

### 100p
```
=== train SingleTransferBERT - 100p ===
  checkpoint = torch.load(model_path)
No checkpoint found. Starting training from scratch...
Training Epoch 1/10: 100% 254/254 [04:54<00:00,  1.16s/it]
Validation: 100% 29/29 [00:10<00:00,  2.65it/s]
Epoch 1/10, Train Loss: 0.5854, Validation Loss: 0.1583, Accuracy: 95.00%
Training Epoch 2/10: 100% 254/254 [04:54<00:00,  1.16s/it]
Validation: 100% 29/29 [00:10<00:00,  2.65it/s]
Epoch 2/10, Train Loss: 0.1249, Validation Loss: 0.1061, Accuracy: 96.67%
Training Epoch 3/10: 100% 254/254 [04:54<00:00,  1.16s/it]
Validation: 100% 29/29 [00:10<00:00,  2.64it/s]
Epoch 3/10, Train Loss: 0.0851, Validation Loss: 0.0980, Accuracy: 97.00%
Training Epoch 4/10: 100% 254/254 [04:54<00:00,  1.16s/it]
Validation: 100% 29/29 [00:10<00:00,  2.64it/s]
Epoch 4/10, Train Loss: 0.0634, Validation Loss: 0.1499, Accuracy: 96.67%
Training Epoch 5/10: 100% 254/254 [04:54<00:00,  1.16s/it]
Validation: 100% 29/29 [00:10<00:00,  2.65it/s]
Epoch 5/10, Train Loss: 0.0546, Validation Loss: 0.0947, Accuracy: 97.33%
Training Epoch 6/10: 100% 254/254 [04:54<00:00,  1.16s/it]
Validation: 100% 29/29 [00:10<00:00,  2.65it/s]
Epoch 6/10, Train Loss: 0.0427, Validation Loss: 0.1196, Accuracy: 96.17%
Training Epoch 7/10: 100% 254/254 [04:54<00:00,  1.16s/it]
Validation: 100% 29/29 [00:10<00:00,  2.64it/s]
Epoch 7/10, Train Loss: 0.0349, Validation Loss: 0.1100, Accuracy: 96.83%
Training Epoch 8/10: 100% 254/254 [04:54<00:00,  1.16s/it]
Validation: 100% 29/29 [00:10<00:00,  2.65it/s]
Epoch 8/10, Train Loss: 0.0274, Validation Loss: 0.1169, Accuracy: 96.61%
Early stopping triggered after epoch 8
=== SingleTransferBERT - 100p training completed ===
```

### 10p
```
=== train SingleTransferBERT - 10p ===
  checkpoint = torch.load(model_path)
No checkpoint found. Starting training from scratch...
Training Epoch 1/10: 100% 26/26 [00:29<00:00,  1.13s/it]
Validation: 100% 3/3 [00:01<00:00,  2.73it/s]
Epoch 1/10, Train Loss: 1.7455, Validation Loss: 1.5922, Accuracy: 38.33%
Training Epoch 2/10: 100% 26/26 [00:29<00:00,  1.14s/it]
Validation: 100% 3/3 [00:01<00:00,  2.73it/s]
Epoch 2/10, Train Loss: 1.2289, Validation Loss: 0.9364, Accuracy: 67.78%
Training Epoch 3/10: 100% 26/26 [00:29<00:00,  1.14s/it]
Validation: 100% 3/3 [00:01<00:00,  2.73it/s]
Epoch 3/10, Train Loss: 0.5698, Validation Loss: 0.5488, Accuracy: 81.11%
Training Epoch 4/10: 100% 26/26 [00:29<00:00,  1.14s/it]
Validation: 100% 3/3 [00:01<00:00,  2.73it/s]
Epoch 4/10, Train Loss: 0.2619, Validation Loss: 0.4443, Accuracy: 84.44%
Training Epoch 5/10: 100% 26/26 [00:29<00:00,  1.14s/it]
Validation: 100% 3/3 [00:01<00:00,  2.73it/s]
Epoch 5/10, Train Loss: 0.1278, Validation Loss: 0.4631, Accuracy: 85.56%
Training Epoch 6/10: 100% 26/26 [00:29<00:00,  1.13s/it]
Validation: 100% 3/3 [00:01<00:00,  2.73it/s]
Epoch 6/10, Train Loss: 0.0681, Validation Loss: 0.4371, Accuracy: 86.11%
Training Epoch 7/10: 100% 26/26 [00:29<00:00,  1.14s/it]
Validation: 100% 3/3 [00:01<00:00,  2.73it/s]
Epoch 7/10, Train Loss: 0.0347, Validation Loss: 0.4588, Accuracy: 86.67%
Training Epoch 8/10: 100% 26/26 [00:29<00:00,  1.13s/it]
Validation: 100% 3/3 [00:01<00:00,  2.73it/s]
Epoch 8/10, Train Loss: 0.0265, Validation Loss: 0.5348, Accuracy: 87.22%
Training Epoch 9/10: 100% 26/26 [00:29<00:00,  1.13s/it]
Validation: 100% 3/3 [00:01<00:00,  2.73it/s]
Epoch 9/10, Train Loss: 0.0159, Validation Loss: 0.4608, Accuracy: 88.89%
Early stopping triggered after epoch 9
=== SingleTransferBERT - 10p training completed ===
```

### 1p
```
=== train SingleTransferBERT - 1p ===
  checkpoint = torch.load(model_path)
No checkpoint found. Starting training from scratch...
Training Epoch 1/10: 100% 3/3 [00:02<00:00,  1.01it/s]
Validation: 100% 1/1 [00:00<00:00,  8.96it/s]
Epoch 1/10, Train Loss: 1.8287, Validation Loss: 1.7990, Accuracy: 16.67%
Training Epoch 2/10: 100% 3/3 [00:03<00:00,  1.01s/it]
Validation: 100% 1/1 [00:00<00:00,  8.92it/s]
Epoch 2/10, Train Loss: 1.7732, Validation Loss: 1.7869, Accuracy: 22.22%
Training Epoch 3/10: 100% 3/3 [00:03<00:00,  1.00s/it]
Validation: 100% 1/1 [00:00<00:00,  8.95it/s]
Epoch 3/10, Train Loss: 1.6804, Validation Loss: 1.7643, Accuracy: 38.89%
Training Epoch 4/10: 100% 3/3 [00:03<00:00,  1.01s/it]
Validation: 100% 1/1 [00:00<00:00,  8.94it/s]
Epoch 4/10, Train Loss: 1.6312, Validation Loss: 1.7427, Accuracy: 27.78%
Training Epoch 5/10: 100% 3/3 [00:03<00:00,  1.00s/it]
Validation: 100% 1/1 [00:00<00:00,  8.72it/s]
Epoch 5/10, Train Loss: 1.5272, Validation Loss: 1.7321, Accuracy: 16.67%
Training Epoch 6/10: 100% 3/3 [00:03<00:00,  1.01s/it]
Validation: 100% 1/1 [00:00<00:00,  8.91it/s]
Epoch 6/10, Train Loss: 1.4273, Validation Loss: 1.7203, Accuracy: 16.67%
Training Epoch 7/10: 100% 3/3 [00:02<00:00,  1.00it/s]
Validation: 100% 1/1 [00:00<00:00,  8.88it/s]
Epoch 7/10, Train Loss: 1.3168, Validation Loss: 1.7105, Accuracy: 16.67%
Training Epoch 8/10: 100% 3/3 [00:03<00:00,  1.02s/it]
Validation: 100% 1/1 [00:00<00:00,  8.92it/s]
Epoch 8/10, Train Loss: 1.1637, Validation Loss: 1.6748, Accuracy: 16.67%
Training Epoch 9/10: 100% 3/3 [00:03<00:00,  1.00s/it]
Validation: 100% 1/1 [00:00<00:00,  8.93it/s]
Epoch 9/10, Train Loss: 1.0525, Validation Loss: 1.6299, Accuracy: 22.22%
Training Epoch 10/10: 100% 3/3 [00:02<00:00,  1.00it/s]
Validation: 100% 1/1 [00:00<00:00,  8.94it/s]
Epoch 10/10, Train Loss: 0.9143, Validation Loss: 1.6321, Accuracy: 22.22%
=== SingleTransferBERT - 1p training completed ===
```
```
=== train SingleTransferBERT - 1p ===
  checkpoint = torch.load(model_path)
No checkpoint found. Starting training from scratch...
Training Epoch 1/100: 100% 3/3 [00:03<00:00,  1.25s/it]
Validation: 100% 1/1 [00:00<00:00,  8.15it/s]
Epoch 1/100, Train Loss: 1.8199, Validation Loss: 1.7673, Accuracy: 27.78%
Training Epoch 2/100: 100% 3/3 [00:03<00:00,  1.01s/it]
Validation: 100% 1/1 [00:00<00:00,  8.93it/s]
Epoch 2/100, Train Loss: 1.7426, Validation Loss: 1.7915, Accuracy: 16.67%
Training Epoch 3/100: 100% 3/3 [00:02<00:00,  1.01it/s]
Validation: 100% 1/1 [00:00<00:00,  8.96it/s]
Epoch 3/100, Train Loss: 1.6681, Validation Loss: 1.7713, Accuracy: 33.33%
Training Epoch 4/100: 100% 3/3 [00:02<00:00,  1.01it/s]
Validation: 100% 1/1 [00:00<00:00,  8.94it/s]
Epoch 4/100, Train Loss: 1.5587, Validation Loss: 1.7533, Accuracy: 27.78%
Training Epoch 5/100: 100% 3/3 [00:03<00:00,  1.01s/it]
Validation: 100% 1/1 [00:00<00:00,  9.00it/s]
Epoch 5/100, Train Loss: 1.4699, Validation Loss: 1.7301, Accuracy: 27.78%
Training Epoch 6/100: 100% 3/3 [00:02<00:00,  1.00it/s]
Validation: 100% 1/1 [00:00<00:00,  8.96it/s]
Epoch 6/100, Train Loss: 1.3520, Validation Loss: 1.7331, Accuracy: 16.67%
Training Epoch 7/100: 100% 3/3 [00:02<00:00,  1.01it/s]
Validation: 100% 1/1 [00:00<00:00,  8.98it/s]
Epoch 7/100, Train Loss: 1.2210, Validation Loss: 1.7407, Accuracy: 22.22%
Training Epoch 8/100: 100% 3/3 [00:02<00:00,  1.01it/s]
Validation: 100% 1/1 [00:00<00:00,  8.97it/s]
Epoch 8/100, Train Loss: 1.1155, Validation Loss: 1.7499, Accuracy: 22.22%
Training Epoch 9/100: 100% 3/3 [00:02<00:00,  1.01it/s]
Validation: 100% 1/1 [00:00<00:00,  8.97it/s]
Epoch 9/100, Train Loss: 0.9492, Validation Loss: 1.7278, Accuracy: 27.78%
Training Epoch 10/100: 100% 3/3 [00:03<00:00,  1.00s/it]
Validation: 100% 1/1 [00:00<00:00,  8.98it/s]
Epoch 10/100, Train Loss: 0.8219, Validation Loss: 1.7059, Accuracy: 33.33%
Training Epoch 11/100: 100% 3/3 [00:02<00:00,  1.00it/s]
Validation: 100% 1/1 [00:00<00:00,  8.99it/s]
Epoch 11/100, Train Loss: 0.7308, Validation Loss: 1.7416, Accuracy: 33.33%
Training Epoch 12/100: 100% 3/3 [00:02<00:00,  1.01it/s]
Validation: 100% 1/1 [00:00<00:00,  9.00it/s]
Epoch 12/100, Train Loss: 0.5944, Validation Loss: 1.7725, Accuracy: 33.33%
Training Epoch 13/100: 100% 3/3 [00:02<00:00,  1.01it/s]
Validation: 100% 1/1 [00:00<00:00,  8.81it/s]
Epoch 13/100, Train Loss: 0.4933, Validation Loss: 1.7652, Accuracy: 33.33%
Training Epoch 14/100: 100% 3/3 [00:02<00:00,  1.01it/s]
Validation: 100% 1/1 [00:00<00:00,  9.00it/s]
Epoch 14/100, Train Loss: 0.4163, Validation Loss: 1.7465, Accuracy: 33.33%
Training Epoch 15/100: 100% 3/3 [00:02<00:00,  1.01it/s]
Validation: 100% 1/1 [00:00<00:00,  8.98it/s]
Epoch 15/100, Train Loss: 0.3325, Validation Loss: 1.7784, Accuracy: 33.33%
Training Epoch 16/100: 100% 3/3 [00:02<00:00,  1.01it/s]
Validation: 100% 1/1 [00:00<00:00,  8.91it/s]
Epoch 16/100, Train Loss: 0.2689, Validation Loss: 1.9007, Accuracy: 33.33%
Training Epoch 17/100: 100% 3/3 [00:02<00:00,  1.01it/s]
Validation: 100% 1/1 [00:00<00:00,  8.99it/s]
Epoch 17/100, Train Loss: 0.2089, Validation Loss: 1.8855, Accuracy: 27.78%
Training Epoch 18/100: 100% 3/3 [00:02<00:00,  1.01it/s]
Validation: 100% 1/1 [00:00<00:00,  8.95it/s]
Epoch 18/100, Train Loss: 0.1720, Validation Loss: 1.7995, Accuracy: 27.78%
Training Epoch 19/100: 100% 3/3 [00:02<00:00,  1.01it/s]
Validation: 100% 1/1 [00:00<00:00,  8.97it/s]
Epoch 19/100, Train Loss: 0.1359, Validation Loss: 1.7963, Accuracy: 38.89%
Training Epoch 20/100: 100% 3/3 [00:02<00:00,  1.01it/s]
Validation: 100% 1/1 [00:00<00:00,  8.98it/s]
Epoch 20/100, Train Loss: 0.1143, Validation Loss: 1.8849, Accuracy: 38.89%
Training Epoch 21/100: 100% 3/3 [00:02<00:00,  1.01it/s]
Validation: 100% 1/1 [00:00<00:00,  8.98it/s]
Epoch 21/100, Train Loss: 0.0927, Validation Loss: 1.9678, Accuracy: 38.89%
Training Epoch 22/100: 100% 3/3 [00:02<00:00,  1.01it/s]
Validation: 100% 1/1 [00:00<00:00,  8.98it/s]
Epoch 22/100, Train Loss: 0.0757, Validation Loss: 1.9579, Accuracy: 38.89%
Training Epoch 23/100: 100% 3/3 [00:02<00:00,  1.01it/s]
Validation: 100% 1/1 [00:00<00:00,  8.97it/s]
Epoch 23/100, Train Loss: 0.0634, Validation Loss: 1.9186, Accuracy: 27.78%
Training Epoch 24/100: 100% 3/3 [00:02<00:00,  1.01it/s]
Validation: 100% 1/1 [00:00<00:00,  8.98it/s]
Epoch 24/100, Train Loss: 0.0539, Validation Loss: 1.9141, Accuracy: 27.78%
Training Epoch 25/100: 100% 3/3 [00:02<00:00,  1.01it/s]
Validation: 100% 1/1 [00:00<00:00,  8.97it/s]
Epoch 25/100, Train Loss: 0.0453, Validation Loss: 1.9443, Accuracy: 27.78%
Training Epoch 26/100: 100% 3/3 [00:02<00:00,  1.01it/s]
Validation: 100% 1/1 [00:00<00:00,  8.97it/s]
Epoch 26/100, Train Loss: 0.0412, Validation Loss: 1.9905, Accuracy: 27.78%
Training Epoch 27/100: 100% 3/3 [00:02<00:00,  1.01it/s]
Validation: 100% 1/1 [00:00<00:00,  8.99it/s]
Epoch 27/100, Train Loss: 0.0346, Validation Loss: 2.0089, Accuracy: 38.89%
Training Epoch 28/100: 100% 3/3 [00:02<00:00,  1.01it/s]
Validation: 100% 1/1 [00:00<00:00,  9.00it/s]
Epoch 28/100, Train Loss: 0.0277, Validation Loss: 2.0146, Accuracy: 38.89%
Training Epoch 29/100: 100% 3/3 [00:02<00:00,  1.01it/s]
Validation: 100% 1/1 [00:00<00:00,  8.94it/s]
Epoch 29/100, Train Loss: 0.0293, Validation Loss: 2.0206, Accuracy: 38.89%
Training Epoch 30/100: 100% 3/3 [00:02<00:00,  1.01it/s]
Validation: 100% 1/1 [00:00<00:00,  8.98it/s]
Epoch 30/100, Train Loss: 0.0245, Validation Loss: 2.0073, Accuracy: 44.44%
Training Epoch 31/100: 100% 3/3 [00:02<00:00,  1.01it/s]
Validation: 100% 1/1 [00:00<00:00,  8.98it/s]
Epoch 31/100, Train Loss: 0.0226, Validation Loss: 1.9986, Accuracy: 38.89%
Training Epoch 32/100: 100% 3/3 [00:02<00:00,  1.01it/s]
Validation: 100% 1/1 [00:00<00:00,  8.97it/s]
Epoch 32/100, Train Loss: 0.0195, Validation Loss: 2.0033, Accuracy: 44.44%
Training Epoch 33/100: 100% 3/3 [00:02<00:00,  1.01it/s]
Validation: 100% 1/1 [00:00<00:00,  8.97it/s]
Epoch 33/100, Train Loss: 0.0180, Validation Loss: 2.0177, Accuracy: 44.44%
Training Epoch 34/100: 100% 3/3 [00:02<00:00,  1.01it/s]
Validation: 100% 1/1 [00:00<00:00,  8.97it/s]
Epoch 34/100, Train Loss: 0.0178, Validation Loss: 2.0344, Accuracy: 44.44%
Training Epoch 35/100: 100% 3/3 [00:02<00:00,  1.01it/s]
Validation: 100% 1/1 [00:00<00:00,  8.95it/s]
Epoch 35/100, Train Loss: 0.0165, Validation Loss: 2.0540, Accuracy: 44.44%
Training Epoch 36/100: 100% 3/3 [00:02<00:00,  1.01it/s]
Validation: 100% 1/1 [00:00<00:00,  8.99it/s]
Epoch 36/100, Train Loss: 0.0148, Validation Loss: 2.0728, Accuracy: 38.89%
Training Epoch 37/100: 100% 3/3 [00:02<00:00,  1.01it/s]
Validation: 100% 1/1 [00:00<00:00,  8.97it/s]
Epoch 37/100, Train Loss: 0.0142, Validation Loss: 2.0963, Accuracy: 38.89%
Training Epoch 38/100: 100% 3/3 [00:02<00:00,  1.01it/s]
Validation: 100% 1/1 [00:00<00:00,  8.95it/s]
Epoch 38/100, Train Loss: 0.0140, Validation Loss: 2.1175, Accuracy: 38.89%
Training Epoch 39/100: 100% 3/3 [00:02<00:00,  1.01it/s]
Validation: 100% 1/1 [00:00<00:00,  9.01it/s]
Epoch 39/100, Train Loss: 0.0139, Validation Loss: 2.1091, Accuracy: 38.89%
Training Epoch 40/100: 100% 3/3 [00:02<00:00,  1.01it/s]
Validation: 100% 1/1 [00:00<00:00,  9.01it/s]
Epoch 40/100, Train Loss: 0.0119, Validation Loss: 2.0758, Accuracy: 33.33%
Early stopping triggered after epoch 40
=== SingleTransferBERT - 1p training completed ===
```

## SingleTransferMLBERT

### 100p
```
=== train SingleTransferMLBERT - 100p ===
  checkpoint = torch.load(model_path)
No checkpoint found. Starting training from scratch...
Training Epoch 1/10: 100% 254/254 [04:57<00:00,  1.17s/it]
Validation: 100% 29/29 [00:10<00:00,  2.64it/s]
Epoch 1/10, Train Loss: 0.6438, Validation Loss: 0.1360, Accuracy: 95.89%
Training Epoch 2/10: 100% 254/254 [04:55<00:00,  1.16s/it]
Validation: 100% 29/29 [00:10<00:00,  2.65it/s]
Epoch 2/10, Train Loss: 0.1523, Validation Loss: 0.1127, Accuracy: 96.44%
Training Epoch 3/10: 100% 254/254 [04:55<00:00,  1.16s/it]
Validation: 100% 29/29 [00:10<00:00,  2.65it/s]
Epoch 3/10, Train Loss: 0.1081, Validation Loss: 0.0975, Accuracy: 96.61%
Training Epoch 4/10: 100% 254/254 [04:55<00:00,  1.16s/it]
Validation: 100% 29/29 [00:10<00:00,  2.65it/s]
Epoch 4/10, Train Loss: 0.0817, Validation Loss: 0.1085, Accuracy: 96.28%
Training Epoch 5/10: 100% 254/254 [04:55<00:00,  1.16s/it]
Validation: 100% 29/29 [00:10<00:00,  2.65it/s]
Epoch 5/10, Train Loss: 0.0725, Validation Loss: 0.1022, Accuracy: 96.78%
Training Epoch 6/10: 100% 254/254 [04:55<00:00,  1.16s/it]
Validation: 100% 29/29 [00:10<00:00,  2.65it/s]
Epoch 6/10, Train Loss: 0.0609, Validation Loss: 0.1014, Accuracy: 96.89%
Early stopping triggered after epoch 6
=== SingleTransferMLBERT - 100p training completed ===
```

### 10p
```
=== train SingleTransferMLBERT - 10p ===
  checkpoint = torch.load(model_path)
No checkpoint found. Starting training from scratch...
Training Epoch 1/10: 100% 26/26 [00:29<00:00,  1.14s/it]
Validation: 100% 3/3 [00:01<00:00,  2.73it/s]
Epoch 1/10, Train Loss: 1.7998, Validation Loss: 1.7597, Accuracy: 24.44%
Training Epoch 2/10: 100% 26/26 [00:29<00:00,  1.15s/it]
Validation: 100% 3/3 [00:01<00:00,  2.72it/s]
Epoch 2/10, Train Loss: 1.5276, Validation Loss: 1.1209, Accuracy: 56.11%
Training Epoch 3/10: 100% 26/26 [00:29<00:00,  1.14s/it]
Validation: 100% 3/3 [00:01<00:00,  2.68it/s]
Epoch 3/10, Train Loss: 0.8098, Validation Loss: 0.7204, Accuracy: 76.67%
Training Epoch 4/10: 100% 26/26 [00:29<00:00,  1.14s/it]
Validation: 100% 3/3 [00:01<00:00,  2.72it/s]
Epoch 4/10, Train Loss: 0.3958, Validation Loss: 0.5996, Accuracy: 81.67%
Training Epoch 5/10: 100% 26/26 [00:29<00:00,  1.14s/it]
Validation: 100% 3/3 [00:01<00:00,  2.71it/s]
Epoch 5/10, Train Loss: 0.1818, Validation Loss: 0.4531, Accuracy: 86.67%
Training Epoch 6/10: 100% 26/26 [00:29<00:00,  1.14s/it]
Validation: 100% 3/3 [00:01<00:00,  2.71it/s]
Epoch 6/10, Train Loss: 0.0903, Validation Loss: 0.4969, Accuracy: 87.22%
Training Epoch 7/10: 100% 26/26 [00:29<00:00,  1.14s/it]
Validation: 100% 3/3 [00:01<00:00,  2.73it/s]
Epoch 7/10, Train Loss: 0.0689, Validation Loss: 0.5425, Accuracy: 87.78%
Training Epoch 8/10: 100% 26/26 [00:29<00:00,  1.14s/it]
Validation: 100% 3/3 [00:01<00:00,  2.73it/s]
Epoch 8/10, Train Loss: 0.0551, Validation Loss: 0.4976, Accuracy: 87.78%
Early stopping triggered after epoch 8
=== SingleTransferMLBERT - 10p training completed ===
```

### 1p
```
=== train SingleTransferMLBERT - 1p ===
  checkpoint = torch.load(model_path)
No checkpoint found. Starting training from scratch...
Training Epoch 1/10: 100% 3/3 [00:02<00:00,  1.01it/s]
Validation: 100% 1/1 [00:00<00:00,  8.93it/s]
Epoch 1/10, Train Loss: 1.8027, Validation Loss: 1.7975, Accuracy: 16.67%
Training Epoch 2/10: 100% 3/3 [00:03<00:00,  1.01s/it]
Validation: 100% 1/1 [00:00<00:00,  8.91it/s]
Epoch 2/10, Train Loss: 1.7897, Validation Loss: 1.7954, Accuracy: 16.67%
Training Epoch 3/10: 100% 3/3 [00:03<00:00,  1.00s/it]
Validation: 100% 1/1 [00:00<00:00,  8.91it/s]
Epoch 3/10, Train Loss: 1.7762, Validation Loss: 1.7856, Accuracy: 16.67%
Training Epoch 4/10: 100% 3/3 [00:03<00:00,  1.00s/it]
Validation: 100% 1/1 [00:00<00:00,  8.85it/s]
Epoch 4/10, Train Loss: 1.7470, Validation Loss: 1.7771, Accuracy: 22.22%
Training Epoch 5/10: 100% 3/3 [00:03<00:00,  1.00s/it]
Validation: 100% 1/1 [00:00<00:00,  8.86it/s]
Epoch 5/10, Train Loss: 1.6866, Validation Loss: 1.7623, Accuracy: 27.78%
Training Epoch 6/10: 100% 3/3 [00:03<00:00,  1.01s/it]
Validation: 100% 1/1 [00:00<00:00,  8.92it/s]
Epoch 6/10, Train Loss: 1.5950, Validation Loss: 1.7136, Accuracy: 38.89%
Training Epoch 7/10: 100% 3/3 [00:03<00:00,  1.01s/it]
Validation: 100% 1/1 [00:00<00:00,  8.85it/s]
Epoch 7/10, Train Loss: 1.4269, Validation Loss: 1.7575, Accuracy: 27.78%
Training Epoch 8/10: 100% 3/3 [00:02<00:00,  1.01it/s]
Validation: 100% 1/1 [00:00<00:00,  8.93it/s]
Epoch 8/10, Train Loss: 1.2373, Validation Loss: 1.7703, Accuracy: 33.33%
Training Epoch 9/10: 100% 3/3 [00:02<00:00,  1.00it/s]
Validation: 100% 1/1 [00:00<00:00,  8.94it/s]
Epoch 9/10, Train Loss: 1.0677, Validation Loss: 1.6764, Accuracy: 50.00%
Training Epoch 10/10: 100% 3/3 [00:03<00:00,  1.01s/it]
Validation: 100% 1/1 [00:00<00:00,  8.88it/s]
Epoch 10/10, Train Loss: 0.9485, Validation Loss: 1.6972, Accuracy: 50.00%
=== SingleTransferMLBERT - 1p training completed ===
```

## DoubleTransferMLBERT

### 100p
```
=== train DoubleTransferMLBERT - 100p ===
  checkpoint = torch.load(model_path)
No checkpoint found. Starting training from scratch...
Training Epoch 1/10: 100% 254/254 [04:57<00:00,  1.17s/it]
Validation: 100% 29/29 [00:10<00:00,  2.64it/s]
Epoch 1/10, Train Loss: 0.5313, Validation Loss: 0.1333, Accuracy: 95.89%
Training Epoch 2/10: 100% 254/254 [04:56<00:00,  1.17s/it]
Validation: 100% 29/29 [00:10<00:00,  2.64it/s]
Epoch 2/10, Train Loss: 0.1363, Validation Loss: 0.1341, Accuracy: 95.67%
Training Epoch 3/10: 100% 254/254 [04:56<00:00,  1.17s/it]
Validation: 100% 29/29 [00:10<00:00,  2.65it/s]
Epoch 3/10, Train Loss: 0.0969, Validation Loss: 0.0946, Accuracy: 96.61%
Training Epoch 4/10: 100% 254/254 [04:56<00:00,  1.17s/it]
Validation: 100% 29/29 [00:10<00:00,  2.65it/s]
Epoch 4/10, Train Loss: 0.0801, Validation Loss: 0.0944, Accuracy: 96.72%
Training Epoch 5/10: 100% 254/254 [04:56<00:00,  1.17s/it]
Validation: 100% 29/29 [00:10<00:00,  2.64it/s]
Epoch 5/10, Train Loss: 0.0722, Validation Loss: 0.0813, Accuracy: 97.11%
Training Epoch 6/10: 100% 254/254 [04:56<00:00,  1.17s/it]
Validation: 100% 29/29 [00:10<00:00,  2.65it/s]
Epoch 6/10, Train Loss: 0.0585, Validation Loss: 0.0951, Accuracy: 97.06%
Training Epoch 7/10: 100% 254/254 [04:56<00:00,  1.17s/it]
Validation: 100% 29/29 [00:10<00:00,  2.64it/s]
Epoch 7/10, Train Loss: 0.0563, Validation Loss: 0.1226, Accuracy: 96.78%
Training Epoch 8/10: 100% 254/254 [04:56<00:00,  1.17s/it]
Validation: 100% 29/29 [00:10<00:00,  2.64it/s]
Epoch 8/10, Train Loss: 0.0483, Validation Loss: 0.1046, Accuracy: 96.56%
Early stopping triggered after epoch 8
=== DoubleTransferMLBERT - 100p training completed ===
```

### 10p
```
=== train DoubleTransferMLBERT - 10p ===
  checkpoint = torch.load(model_path)
No checkpoint found. Starting training from scratch...
Training Epoch 1/10: 100% 26/26 [00:29<00:00,  1.14s/it]
Validation: 100% 3/3 [00:01<00:00,  2.72it/s]
Epoch 1/10, Train Loss: 1.6574, Validation Loss: 1.4411, Accuracy: 36.67%
Training Epoch 2/10: 100% 26/26 [00:29<00:00,  1.14s/it]
Validation: 100% 3/3 [00:01<00:00,  2.73it/s]
Epoch 2/10, Train Loss: 1.1993, Validation Loss: 1.0565, Accuracy: 57.78%
Training Epoch 3/10: 100% 26/26 [00:29<00:00,  1.14s/it]
Validation: 100% 3/3 [00:01<00:00,  2.73it/s]
Epoch 3/10, Train Loss: 0.6663, Validation Loss: 0.5373, Accuracy: 80.56%
Training Epoch 4/10: 100% 26/26 [00:29<00:00,  1.14s/it]
Validation: 100% 3/3 [00:01<00:00,  2.73it/s]
Epoch 4/10, Train Loss: 0.3471, Validation Loss: 0.4454, Accuracy: 86.11%
Training Epoch 5/10: 100% 26/26 [00:29<00:00,  1.14s/it]
Validation: 100% 3/3 [00:01<00:00,  2.73it/s]
Epoch 5/10, Train Loss: 0.1749, Validation Loss: 0.3657, Accuracy: 88.89%
Training Epoch 6/10: 100% 26/26 [00:29<00:00,  1.15s/it]
Validation: 100% 3/3 [00:01<00:00,  2.73it/s]
Epoch 6/10, Train Loss: 0.0934, Validation Loss: 0.3183, Accuracy: 91.11%
Training Epoch 7/10: 100% 26/26 [00:29<00:00,  1.14s/it]
Validation: 100% 3/3 [00:01<00:00,  2.70it/s]
Epoch 7/10, Train Loss: 0.0602, Validation Loss: 0.3734, Accuracy: 90.56%
Training Epoch 8/10: 100% 26/26 [00:29<00:00,  1.14s/it]
Validation: 100% 3/3 [00:01<00:00,  2.73it/s]
Epoch 8/10, Train Loss: 0.0340, Validation Loss: 0.4195, Accuracy: 90.56%
Training Epoch 9/10: 100% 26/26 [00:29<00:00,  1.14s/it]
Validation: 100% 3/3 [00:01<00:00,  2.73it/s]
Epoch 9/10, Train Loss: 0.0336, Validation Loss: 0.4386, Accuracy: 89.44%
Early stopping triggered after epoch 9
=== DoubleTransferMLBERT - 10p training completed ===
```

### 1p
```
=== train DoubleTransferMLBERT - 1p ===
  checkpoint = torch.load(model_path)
No checkpoint found. Starting training from scratch...
Training Epoch 1/10: 100% 3/3 [00:02<00:00,  1.01it/s]
Validation: 100% 1/1 [00:00<00:00,  8.97it/s]
Epoch 1/10, Train Loss: 1.8166, Validation Loss: 1.7827, Accuracy: 22.22%
Training Epoch 2/10: 100% 3/3 [00:03<00:00,  1.01s/it]
Validation: 100% 1/1 [00:00<00:00,  8.92it/s]
Epoch 2/10, Train Loss: 1.7409, Validation Loss: 1.7760, Accuracy: 16.67%
Training Epoch 3/10: 100% 3/3 [00:03<00:00,  1.00s/it]
Validation: 100% 1/1 [00:00<00:00,  8.93it/s]
Epoch 3/10, Train Loss: 1.6650, Validation Loss: 1.7568, Accuracy: 27.78%
Training Epoch 4/10: 100% 3/3 [00:03<00:00,  1.01s/it]
Validation: 100% 1/1 [00:00<00:00,  8.96it/s]
Epoch 4/10, Train Loss: 1.5571, Validation Loss: 1.7463, Accuracy: 16.67%
Training Epoch 5/10: 100% 3/3 [00:03<00:00,  1.00s/it]
Validation: 100% 1/1 [00:00<00:00,  8.96it/s]
Epoch 5/10, Train Loss: 1.4823, Validation Loss: 1.7424, Accuracy: 22.22%
Training Epoch 6/10: 100% 3/3 [00:03<00:00,  1.01s/it]
Validation: 100% 1/1 [00:00<00:00,  8.95it/s]
Epoch 6/10, Train Loss: 1.2740, Validation Loss: 1.6847, Accuracy: 33.33%
Training Epoch 7/10: 100% 3/3 [00:03<00:00,  1.01s/it]
Validation: 100% 1/1 [00:00<00:00,  8.92it/s]
Epoch 7/10, Train Loss: 1.1069, Validation Loss: 1.6673, Accuracy: 33.33%
Training Epoch 8/10: 100% 3/3 [00:03<00:00,  1.01s/it]
Validation: 100% 1/1 [00:00<00:00,  8.95it/s]
Epoch 8/10, Train Loss: 0.9691, Validation Loss: 1.6711, Accuracy: 38.89%
Training Epoch 9/10: 100% 3/3 [00:02<00:00,  1.01it/s]
Validation: 100% 1/1 [00:00<00:00,  8.93it/s]
Epoch 9/10, Train Loss: 0.7774, Validation Loss: 1.6078, Accuracy: 44.44%
Training Epoch 10/10: 100% 3/3 [00:03<00:00,  1.01s/it]
Validation: 100% 1/1 [00:00<00:00,  8.95it/s]
Epoch 10/10, Train Loss: 0.6162, Validation Loss: 1.6773, Accuracy: 33.33%
=== DoubleTransferMLBERT - 1p training completed ===
```

## BERTsmall

### 100p
```
=== train BERTsmall - 100p ===
  checkpoint = torch.load(model_path)
No checkpoint found. Starting training from scratch...
Training Epoch 1/10: 100% 254/254 [00:57<00:00,  4.40it/s]
Validation: 100% 29/29 [00:02<00:00, 11.05it/s]
Epoch 1/10, Train Loss: 0.9777, Validation Loss: 0.3213, Accuracy: 90.39%
Training Epoch 2/10: 100% 254/254 [00:56<00:00,  4.51it/s]
Validation: 100% 29/29 [00:02<00:00, 11.26it/s]
Epoch 2/10, Train Loss: 0.2638, Validation Loss: 0.1874, Accuracy: 93.89%
Training Epoch 3/10: 100% 254/254 [00:56<00:00,  4.51it/s]
Validation: 100% 29/29 [00:02<00:00, 11.13it/s]
Epoch 3/10, Train Loss: 0.1536, Validation Loss: 0.1435, Accuracy: 95.28%
Training Epoch 4/10: 100% 254/254 [00:56<00:00,  4.52it/s]
Validation: 100% 29/29 [00:02<00:00, 11.22it/s]
Epoch 4/10, Train Loss: 0.1126, Validation Loss: 0.1399, Accuracy: 96.00%
Training Epoch 5/10: 100% 254/254 [00:56<00:00,  4.51it/s]
Validation: 100% 29/29 [00:02<00:00, 11.22it/s]
Epoch 5/10, Train Loss: 0.0876, Validation Loss: 0.1466, Accuracy: 95.00%
Training Epoch 6/10: 100% 254/254 [00:56<00:00,  4.52it/s]
Validation: 100% 29/29 [00:02<00:00, 11.27it/s]
Epoch 6/10, Train Loss: 0.0765, Validation Loss: 0.1572, Accuracy: 96.00%
Training Epoch 7/10: 100% 254/254 [00:56<00:00,  4.52it/s]
Validation: 100% 29/29 [00:02<00:00, 11.11it/s]
Epoch 7/10, Train Loss: 0.0673, Validation Loss: 0.1347, Accuracy: 95.78%
Training Epoch 8/10: 100% 254/254 [00:56<00:00,  4.50it/s]
Validation: 100% 29/29 [00:02<00:00, 11.12it/s]
Epoch 8/10, Train Loss: 0.0584, Validation Loss: 0.1216, Accuracy: 96.89%
Training Epoch 9/10: 100% 254/254 [00:56<00:00,  4.51it/s]
Validation: 100% 29/29 [00:02<00:00, 11.21it/s]
Epoch 9/10, Train Loss: 0.0456, Validation Loss: 0.1193, Accuracy: 96.11%
Training Epoch 10/10: 100% 254/254 [00:56<00:00,  4.50it/s]
Validation: 100% 29/29 [00:02<00:00, 11.20it/s]
Epoch 10/10, Train Loss: 0.0436, Validation Loss: 0.1370, Accuracy: 95.61%
=== BERTsmall - 100p training completed ===
```

### 10p
```
=== train BERTsmall - 10p ===
  checkpoint = torch.load(model_path)
No checkpoint found. Starting training from scratch...
Training Epoch 1/10:  65% 17/26 [00:03<00:02,  4.49it/s]
model.safetensors:   0% 0.00/116M [00:00<?, ?B/s]
Training Epoch 1/10:  69% 18/26 [00:04<00:01,  4.49it/s]
Training Epoch 1/10:  73% 19/26 [00:04<00:01,  4.46it/s]
model.safetensors:  63% 73.4M/116M [00:00<00:00, 171MB/s]
Training Epoch 1/10:  77% 20/26 [00:04<00:01,  4.45it/s]
model.safetensors: 100% 116M/116M [00:00<00:00, 169MB/s]
Training Epoch 1/10: 100% 26/26 [00:05<00:00,  4.56it/s]
Validation: 100% 3/3 [00:00<00:00, 11.45it/s]
Epoch 1/10, Train Loss: 1.7989, Validation Loss: 1.7245, Accuracy: 26.11%
Training Epoch 2/10: 100% 26/26 [00:05<00:00,  4.62it/s]
Validation: 100% 3/3 [00:00<00:00, 11.57it/s]
Epoch 2/10, Train Loss: 1.6212, Validation Loss: 1.5673, Accuracy: 41.11%
Training Epoch 3/10: 100% 26/26 [00:05<00:00,  4.60it/s]
Validation: 100% 3/3 [00:00<00:00, 11.54it/s]
Epoch 3/10, Train Loss: 1.3765, Validation Loss: 1.3539, Accuracy: 50.00%
Training Epoch 4/10: 100% 26/26 [00:05<00:00,  4.63it/s]
Validation: 100% 3/3 [00:00<00:00, 11.50it/s]
Epoch 4/10, Train Loss: 1.0636, Validation Loss: 0.9902, Accuracy: 62.22%
Training Epoch 5/10: 100% 26/26 [00:05<00:00,  4.62it/s]
Validation: 100% 3/3 [00:00<00:00, 11.47it/s]
Epoch 5/10, Train Loss: 0.7910, Validation Loss: 0.7606, Accuracy: 71.11%
Training Epoch 6/10: 100% 26/26 [00:05<00:00,  4.62it/s]
Validation: 100% 3/3 [00:00<00:00, 11.50it/s]
Epoch 6/10, Train Loss: 0.5911, Validation Loss: 0.6073, Accuracy: 77.78%
Training Epoch 7/10: 100% 26/26 [00:05<00:00,  4.63it/s]
Validation: 100% 3/3 [00:00<00:00, 11.48it/s]
Epoch 7/10, Train Loss: 0.4463, Validation Loss: 0.5083, Accuracy: 81.67%
Training Epoch 8/10: 100% 26/26 [00:05<00:00,  4.61it/s]
Validation: 100% 3/3 [00:00<00:00, 11.53it/s]
Epoch 8/10, Train Loss: 0.3517, Validation Loss: 0.4811, Accuracy: 80.56%
Training Epoch 9/10: 100% 26/26 [00:05<00:00,  4.63it/s]
Validation: 100% 3/3 [00:00<00:00, 11.51it/s]
Epoch 9/10, Train Loss: 0.2651, Validation Loss: 0.4138, Accuracy: 85.56%
Training Epoch 10/10: 100% 26/26 [00:05<00:00,  4.61it/s]
Validation: 100% 3/3 [00:00<00:00, 11.54it/s]
Epoch 10/10, Train Loss: 0.2098, Validation Loss: 0.4102, Accuracy: 86.11%
=== BERTsmall - 10p training completed ===
```
```
=== train BERTsmall - 10p ===
  checkpoint = torch.load(model_path)
model.safetensors: 100% 116M/116M [00:00<00:00, 177MB/s]
Resuming training from epoch 10...
Training Epoch 11/100: 100% 26/26 [00:06<00:00,  4.05it/s]
Validation: 100% 3/3 [00:00<00:00, 10.86it/s]
Epoch 11/100, Train Loss: 0.1630, Validation Loss: 0.3890, Accuracy: 87.78%
Training Epoch 12/100: 100% 26/26 [00:05<00:00,  4.60it/s]
Validation: 100% 3/3 [00:00<00:00, 11.57it/s]
Epoch 12/100, Train Loss: 0.1254, Validation Loss: 0.3686, Accuracy: 87.78%
Training Epoch 13/100: 100% 26/26 [00:05<00:00,  4.61it/s]
Validation: 100% 3/3 [00:00<00:00, 11.44it/s]
Epoch 13/100, Train Loss: 0.0973, Validation Loss: 0.3809, Accuracy: 87.22%
Training Epoch 14/100: 100% 26/26 [00:05<00:00,  4.59it/s]
Validation: 100% 3/3 [00:00<00:00, 11.34it/s]
Epoch 14/100, Train Loss: 0.0829, Validation Loss: 0.3909, Accuracy: 87.78%
Training Epoch 15/100: 100% 26/26 [00:05<00:00,  4.62it/s]
Validation: 100% 3/3 [00:00<00:00, 11.37it/s]
Epoch 15/100, Train Loss: 0.0634, Validation Loss: 0.3741, Accuracy: 87.78%
Training Epoch 16/100: 100% 26/26 [00:05<00:00,  4.62it/s]
Validation: 100% 3/3 [00:00<00:00, 11.43it/s]
Epoch 16/100, Train Loss: 0.0502, Validation Loss: 0.3806, Accuracy: 88.33%
Training Epoch 17/100: 100% 26/26 [00:05<00:00,  4.62it/s]
Validation: 100% 3/3 [00:00<00:00, 11.39it/s]
Epoch 17/100, Train Loss: 0.0373, Validation Loss: 0.3882, Accuracy: 87.22%
Training Epoch 18/100: 100% 26/26 [00:05<00:00,  4.62it/s]
Validation: 100% 3/3 [00:00<00:00, 11.51it/s]
Epoch 18/100, Train Loss: 0.0394, Validation Loss: 0.3798, Accuracy: 86.67%
Training Epoch 19/100: 100% 26/26 [00:05<00:00,  4.62it/s]
Validation: 100% 3/3 [00:00<00:00, 11.47it/s]
Epoch 19/100, Train Loss: 0.0342, Validation Loss: 0.3988, Accuracy: 87.22%
Training Epoch 20/100: 100% 26/26 [00:05<00:00,  4.62it/s]
Validation: 100% 3/3 [00:00<00:00, 11.54it/s]
Epoch 20/100, Train Loss: 0.0258, Validation Loss: 0.3562, Accuracy: 89.44%
Training Epoch 21/100: 100% 26/26 [00:05<00:00,  4.62it/s]
Validation: 100% 3/3 [00:00<00:00, 11.51it/s]
Epoch 21/100, Train Loss: 0.0178, Validation Loss: 0.4212, Accuracy: 87.78%
Training Epoch 22/100: 100% 26/26 [00:05<00:00,  4.62it/s]
Validation: 100% 3/3 [00:00<00:00, 11.41it/s]
Epoch 22/100, Train Loss: 0.0172, Validation Loss: 0.3904, Accuracy: 88.89%
Training Epoch 23/100: 100% 26/26 [00:05<00:00,  4.62it/s]
Validation: 100% 3/3 [00:00<00:00, 11.45it/s]
Epoch 23/100, Train Loss: 0.0178, Validation Loss: 0.4112, Accuracy: 88.89%
Training Epoch 24/100: 100% 26/26 [00:05<00:00,  4.57it/s]
Validation: 100% 3/3 [00:00<00:00, 11.44it/s]
Epoch 24/100, Train Loss: 0.0176, Validation Loss: 0.3989, Accuracy: 87.22%
Training Epoch 25/100: 100% 26/26 [00:05<00:00,  4.62it/s]
Validation: 100% 3/3 [00:00<00:00, 11.44it/s]
Epoch 25/100, Train Loss: 0.0116, Validation Loss: 0.3973, Accuracy: 88.89%
Training Epoch 26/100: 100% 26/26 [00:05<00:00,  4.61it/s]
Validation: 100% 3/3 [00:00<00:00, 11.52it/s]
Epoch 26/100, Train Loss: 0.0124, Validation Loss: 0.4106, Accuracy: 88.89%
Training Epoch 27/100: 100% 26/26 [00:05<00:00,  4.62it/s]
Validation: 100% 3/3 [00:00<00:00, 11.50it/s]
Epoch 27/100, Train Loss: 0.0116, Validation Loss: 0.4043, Accuracy: 88.33%
Training Epoch 28/100: 100% 26/26 [00:05<00:00,  4.62it/s]
Validation: 100% 3/3 [00:00<00:00, 11.54it/s]
Epoch 28/100, Train Loss: 0.0089, Validation Loss: 0.4344, Accuracy: 88.33%
Training Epoch 29/100: 100% 26/26 [00:05<00:00,  4.62it/s]
Validation: 100% 3/3 [00:00<00:00, 11.45it/s]
Epoch 29/100, Train Loss: 0.0093, Validation Loss: 0.4412, Accuracy: 88.33%
Training Epoch 30/100: 100% 26/26 [00:05<00:00,  4.61it/s]
Validation: 100% 3/3 [00:00<00:00, 11.53it/s]
Epoch 30/100, Train Loss: 0.0080, Validation Loss: 0.4047, Accuracy: 88.89%
Early stopping triggered after epoch 30
=== BERTsmall - 10p training completed ===
```

### 1p
```
=== train BERTsmall - 1p ===
  checkpoint = torch.load(model_path)
No checkpoint found. Starting training from scratch...
Training Epoch 1/10: 100% 3/3 [00:00<00:00,  5.07it/s]
Validation: 100% 1/1 [00:00<00:00, 35.24it/s]
Epoch 1/10, Train Loss: 1.8392, Validation Loss: 1.6576, Accuracy: 33.33%
Training Epoch 2/10: 100% 3/3 [00:00<00:00,  5.23it/s]
Validation: 100% 1/1 [00:00<00:00, 35.99it/s]
Epoch 2/10, Train Loss: 1.7587, Validation Loss: 1.6325, Accuracy: 38.89%
Training Epoch 3/10: 100% 3/3 [00:00<00:00,  5.26it/s]
Validation: 100% 1/1 [00:00<00:00, 35.88it/s]
Epoch 3/10, Train Loss: 1.7142, Validation Loss: 1.6193, Accuracy: 44.44%
Training Epoch 4/10: 100% 3/3 [00:00<00:00,  5.23it/s]
Validation: 100% 1/1 [00:00<00:00, 35.80it/s]
Epoch 4/10, Train Loss: 1.6942, Validation Loss: 1.6111, Accuracy: 33.33%
Training Epoch 5/10: 100% 3/3 [00:00<00:00,  5.15it/s]
Validation: 100% 1/1 [00:00<00:00, 35.53it/s]
Epoch 5/10, Train Loss: 1.5851, Validation Loss: 1.6070, Accuracy: 33.33%
Training Epoch 6/10: 100% 3/3 [00:00<00:00,  4.87it/s]
Validation: 100% 1/1 [00:00<00:00, 35.64it/s]
Epoch 6/10, Train Loss: 1.5297, Validation Loss: 1.5924, Accuracy: 33.33%
Training Epoch 7/10: 100% 3/3 [00:00<00:00,  5.24it/s]
Validation: 100% 1/1 [00:00<00:00, 34.62it/s]
Epoch 7/10, Train Loss: 1.4938, Validation Loss: 1.5728, Accuracy: 33.33%
Training Epoch 8/10: 100% 3/3 [00:00<00:00,  5.24it/s]
Validation: 100% 1/1 [00:00<00:00, 35.79it/s]
Epoch 8/10, Train Loss: 1.4333, Validation Loss: 1.5538, Accuracy: 50.00%
Training Epoch 9/10: 100% 3/3 [00:00<00:00,  5.22it/s]
Validation: 100% 1/1 [00:00<00:00, 34.39it/s]
Epoch 9/10, Train Loss: 1.3611, Validation Loss: 1.5377, Accuracy: 50.00%
Training Epoch 10/10: 100% 3/3 [00:00<00:00,  5.22it/s]
Validation: 100% 1/1 [00:00<00:00, 33.81it/s]
Epoch 10/10, Train Loss: 1.3030, Validation Loss: 1.5270, Accuracy: 50.00%
=== BERTsmall - 1p training completed ===
```

## BERTlarge

### 100p
```
=== train BERTlarge - 100p ===
  checkpoint = torch.load(model_path)
No checkpoint found. Starting training from scratch...
Training Epoch 1/10: 100% 507/507 [15:59<00:00,  1.89s/it]
Validation: 100% 57/57 [00:34<00:00,  1.65it/s]
Epoch 1/10, Train Loss: 0.4365, Validation Loss: 0.1460, Accuracy: 95.33%
Training Epoch 2/10: 100% 507/507 [15:57<00:00,  1.89s/it]
Validation: 100% 57/57 [00:34<00:00,  1.65it/s]
Epoch 2/10, Train Loss: 0.1094, Validation Loss: 0.0951, Accuracy: 96.72%
Training Epoch 3/10: 100% 507/507 [15:57<00:00,  1.89s/it]
Validation: 100% 57/57 [00:34<00:00,  1.65it/s]
Epoch 3/10, Train Loss: 0.0793, Validation Loss: 0.1239, Accuracy: 95.28%
Training Epoch 4/10: 100% 507/507 [15:57<00:00,  1.89s/it]
Validation: 100% 57/57 [00:34<00:00,  1.65it/s]
Epoch 4/10, Train Loss: 0.0618, Validation Loss: 0.1173, Accuracy: 96.61%
Training Epoch 5/10: 100% 507/507 [15:57<00:00,  1.89s/it]
Validation: 100% 57/57 [00:34<00:00,  1.65it/s]
Epoch 5/10, Train Loss: 0.0569, Validation Loss: 0.1279, Accuracy: 96.94%
Early stopping triggered after epoch 5
=== BERTlarge - 100p training completed ===
```

### 10p
```
=== train BERTlarge - 10p ===
  checkpoint = torch.load(model_path)
No checkpoint found. Starting training from scratch...
Training Epoch 1/10: 100% 51/51 [01:35<00:00,  1.88s/it]
Validation: 100% 6/6 [00:03<00:00,  1.73it/s]
Epoch 1/10, Train Loss: 1.6343, Validation Loss: 1.2827, Accuracy: 52.78%
Training Epoch 2/10: 100% 51/51 [01:35<00:00,  1.88s/it]
Validation: 100% 6/6 [00:03<00:00,  1.74it/s]
Epoch 2/10, Train Loss: 0.8193, Validation Loss: 0.6713, Accuracy: 75.00%
Training Epoch 3/10: 100% 51/51 [01:35<00:00,  1.88s/it]
Validation: 100% 6/6 [00:03<00:00,  1.74it/s]
Epoch 3/10, Train Loss: 0.3678, Validation Loss: 0.5577, Accuracy: 83.33%
Training Epoch 4/10: 100% 51/51 [01:35<00:00,  1.88s/it]
Validation: 100% 6/6 [00:03<00:00,  1.74it/s]
Epoch 4/10, Train Loss: 0.1503, Validation Loss: 0.4285, Accuracy: 86.11%
Training Epoch 5/10: 100% 51/51 [01:35<00:00,  1.88s/it]
Validation: 100% 6/6 [00:03<00:00,  1.74it/s]
Epoch 5/10, Train Loss: 0.0563, Validation Loss: 0.4928, Accuracy: 85.00%
Training Epoch 6/10: 100% 51/51 [01:35<00:00,  1.88s/it]
Validation: 100% 6/6 [00:03<00:00,  1.74it/s]
Epoch 6/10, Train Loss: 0.0287, Validation Loss: 0.4672, Accuracy: 85.56%
Training Epoch 7/10: 100% 51/51 [01:35<00:00,  1.88s/it]
Validation: 100% 6/6 [00:03<00:00,  1.74it/s]
Epoch 7/10, Train Loss: 0.0211, Validation Loss: 0.4906, Accuracy: 88.33%
Early stopping triggered after epoch 7
=== BERTlarge - 10p training completed ===
```

### 1p
```
=== train BERTlarge - 1p ===
  checkpoint = torch.load(model_path)
No checkpoint found. Starting training from scratch...
Training Epoch 1/10: 100% 6/6 [00:09<00:00,  1.60s/it]
Validation: 100% 1/1 [00:00<00:00,  2.82it/s]
Epoch 1/10, Train Loss: 1.8204, Validation Loss: 1.7641, Accuracy: 27.78%
Training Epoch 2/10: 100% 6/6 [00:09<00:00,  1.61s/it]
Validation: 100% 1/1 [00:00<00:00,  2.82it/s]
Epoch 2/10, Train Loss: 1.5960, Validation Loss: 1.7632, Accuracy: 11.11%
Training Epoch 3/10: 100% 6/6 [00:09<00:00,  1.61s/it]
Validation: 100% 1/1 [00:00<00:00,  2.82it/s]
Epoch 3/10, Train Loss: 1.4522, Validation Loss: 1.7788, Accuracy: 16.67%
Training Epoch 4/10: 100% 6/6 [00:09<00:00,  1.60s/it]
Validation: 100% 1/1 [00:00<00:00,  2.79it/s]
Epoch 4/10, Train Loss: 1.3350, Validation Loss: 1.7934, Accuracy: 16.67%
Training Epoch 5/10: 100% 6/6 [00:09<00:00,  1.61s/it]
Validation: 100% 1/1 [00:00<00:00,  2.82it/s]
Epoch 5/10, Train Loss: 1.1159, Validation Loss: 1.7812, Accuracy: 16.67%
Early stopping triggered after epoch 5
=== BERTlarge - 1p training completed ===
```

## 5p data Training Result

# BERTsmall
```
=== train BERTsmall - 5p ===
  checkpoint = torch.load(model_path)
No checkpoint found. Starting training from scratch...
Training Epoch 1/10: 100% 13/13 [00:02<00:00,  4.54it/s]
Validation: 100% 2/2 [00:00<00:00, 13.43it/s]
Epoch 1/10, Train Loss: 1.8198, Validation Loss: 1.7538, Accuracy: 17.78%
Training Epoch 2/10: 100% 13/13 [00:02<00:00,  4.58it/s]
Validation: 100% 2/2 [00:00<00:00, 14.87it/s]
Epoch 2/10, Train Loss: 1.7262, Validation Loss: 1.7200, Accuracy: 25.56%
Training Epoch 3/10: 100% 13/13 [00:02<00:00,  4.54it/s]
Validation: 100% 2/2 [00:00<00:00, 14.84it/s]
Epoch 3/10, Train Loss: 1.6086, Validation Loss: 1.6283, Accuracy: 31.11%
Training Epoch 4/10: 100% 13/13 [00:02<00:00,  4.57it/s]
Validation: 100% 2/2 [00:00<00:00, 14.81it/s]
Epoch 4/10, Train Loss: 1.4962, Validation Loss: 1.6236, Accuracy: 38.89%
Training Epoch 5/10: 100% 13/13 [00:02<00:00,  4.58it/s]
Validation: 100% 2/2 [00:00<00:00, 14.58it/s]
Epoch 5/10, Train Loss: 1.3246, Validation Loss: 1.3890, Accuracy: 47.78%
Training Epoch 6/10: 100% 13/13 [00:02<00:00,  4.53it/s]
Validation: 100% 2/2 [00:00<00:00, 14.83it/s]
Epoch 6/10, Train Loss: 1.1356, Validation Loss: 1.2604, Accuracy: 53.33%
Training Epoch 7/10: 100% 13/13 [00:02<00:00,  4.57it/s]
Validation: 100% 2/2 [00:00<00:00, 14.84it/s]
Epoch 7/10, Train Loss: 0.9346, Validation Loss: 1.1801, Accuracy: 55.56%
Training Epoch 8/10: 100% 13/13 [00:02<00:00,  4.59it/s]
Validation: 100% 2/2 [00:00<00:00, 14.89it/s]
Epoch 8/10, Train Loss: 0.7661, Validation Loss: 1.0059, Accuracy: 63.33%
Training Epoch 9/10: 100% 13/13 [00:02<00:00,  4.50it/s]
Validation: 100% 2/2 [00:00<00:00, 14.63it/s]
Epoch 9/10, Train Loss: 0.6179, Validation Loss: 0.9159, Accuracy: 62.22%
Training Epoch 10/10: 100% 13/13 [00:02<00:00,  4.58it/s]
Validation: 100% 2/2 [00:00<00:00, 14.84it/s]
Epoch 10/10, Train Loss: 0.5062, Validation Loss: 0.8759, Accuracy: 64.44%
=== BERTsmall - 5p training completed ===
```
```
=== train BERTsmall - 5p ===
  checkpoint = torch.load(model_path)
Resuming training from epoch 10...
Training Epoch 11/30: 100% 13/13 [00:03<00:00,  3.59it/s]
Validation: 100% 2/2 [00:00<00:00, 13.67it/s]
Epoch 11/30, Train Loss: 0.4003, Validation Loss: 0.8605, Accuracy: 67.78%
Training Epoch 12/30: 100% 13/13 [00:02<00:00,  4.58it/s]
Validation: 100% 2/2 [00:00<00:00, 14.72it/s]
Epoch 12/30, Train Loss: 0.3181, Validation Loss: 0.7480, Accuracy: 68.89%
Training Epoch 13/30: 100% 13/13 [00:02<00:00,  4.59it/s]
Validation: 100% 2/2 [00:00<00:00, 14.89it/s]
Epoch 13/30, Train Loss: 0.2594, Validation Loss: 0.8026, Accuracy: 67.78%
Training Epoch 14/30: 100% 13/13 [00:02<00:00,  4.59it/s]
Validation: 100% 2/2 [00:00<00:00, 14.84it/s]
Epoch 14/30, Train Loss: 0.2065, Validation Loss: 0.7871, Accuracy: 72.22%
Training Epoch 15/30: 100% 13/13 [00:02<00:00,  4.52it/s]
Validation: 100% 2/2 [00:00<00:00, 14.81it/s]
Epoch 15/30, Train Loss: 0.1658, Validation Loss: 0.7655, Accuracy: 70.00%
Early stopping triggered after epoch 15
=== BERTsmall - 5p training completed ===
```

# SingleTransferBERT
```
=== train SingleTransferBERT - 5p ===
  checkpoint = torch.load(model_path)
No checkpoint found. Starting training from scratch...
Training Epoch 1/10: 100% 13/13 [00:16<00:00,  1.25s/it]
Validation: 100% 2/2 [00:00<00:00,  3.38it/s]
Epoch 1/10, Train Loss: 1.7957, Validation Loss: 1.7760, Accuracy: 27.78%
Training Epoch 2/10: 100% 13/13 [00:14<00:00,  1.14s/it]
Validation: 100% 2/2 [00:00<00:00,  3.57it/s]
Epoch 2/10, Train Loss: 1.7109, Validation Loss: 1.6723, Accuracy: 33.33%
Training Epoch 3/10: 100% 13/13 [00:14<00:00,  1.14s/it]
Validation: 100% 2/2 [00:00<00:00,  3.61it/s]
Epoch 3/10, Train Loss: 1.4605, Validation Loss: 1.3727, Accuracy: 48.89%
Training Epoch 4/10: 100% 13/13 [00:14<00:00,  1.14s/it]
Validation: 100% 2/2 [00:00<00:00,  3.62it/s]
Epoch 4/10, Train Loss: 1.0641, Validation Loss: 1.1105, Accuracy: 53.33%
Training Epoch 5/10: 100% 13/13 [00:14<00:00,  1.14s/it]
Validation: 100% 2/2 [00:00<00:00,  3.62it/s]
Epoch 5/10, Train Loss: 0.6610, Validation Loss: 0.8883, Accuracy: 67.78%
Training Epoch 6/10: 100% 13/13 [00:14<00:00,  1.14s/it]
Validation: 100% 2/2 [00:00<00:00,  3.54it/s]
Epoch 6/10, Train Loss: 0.3656, Validation Loss: 0.7179, Accuracy: 73.33%
Training Epoch 7/10: 100% 13/13 [00:14<00:00,  1.14s/it]
Validation: 100% 2/2 [00:00<00:00,  3.60it/s]
Epoch 7/10, Train Loss: 0.1954, Validation Loss: 0.7405, Accuracy: 75.56%
Training Epoch 8/10: 100% 13/13 [00:14<00:00,  1.14s/it]
Validation: 100% 2/2 [00:00<00:00,  3.62it/s]
Epoch 8/10, Train Loss: 0.1045, Validation Loss: 0.7554, Accuracy: 72.22%
Training Epoch 9/10: 100% 13/13 [00:14<00:00,  1.13s/it]
Validation: 100% 2/2 [00:00<00:00,  3.62it/s]
Epoch 9/10, Train Loss: 0.0537, Validation Loss: 0.7438, Accuracy: 76.67%
Early stopping triggered after epoch 9
=== SingleTransferBERT - 5p training completed ===
```

# BERTlarge
```
=== train BERTlarge - 5p ===
  checkpoint = torch.load(model_path)
No checkpoint found. Starting training from scratch...
Training Epoch 1/10: 100% 26/26 [00:48<00:00,  1.85s/it]
Validation: 100% 3/3 [00:01<00:00,  1.72it/s]
Epoch 1/10, Train Loss: 1.8044, Validation Loss: 1.7820, Accuracy: 22.22%
Training Epoch 2/10: 100% 26/26 [00:48<00:00,  1.85s/it]
Validation: 100% 3/3 [00:01<00:00,  1.72it/s]
Epoch 2/10, Train Loss: 1.6196, Validation Loss: 1.5721, Accuracy: 38.89%
Training Epoch 3/10: 100% 26/26 [00:48<00:00,  1.85s/it]
Validation: 100% 3/3 [00:01<00:00,  1.72it/s]
Epoch 3/10, Train Loss: 1.1895, Validation Loss: 1.2017, Accuracy: 58.89%
Training Epoch 4/10: 100% 26/26 [00:48<00:00,  1.85s/it]
Validation: 100% 3/3 [00:01<00:00,  1.72it/s]
Epoch 4/10, Train Loss: 0.6059, Validation Loss: 0.8998, Accuracy: 68.89%
Training Epoch 5/10: 100% 26/26 [00:48<00:00,  1.85s/it]
Validation: 100% 3/3 [00:01<00:00,  1.72it/s]
Epoch 5/10, Train Loss: 0.2631, Validation Loss: 0.9228, Accuracy: 70.00%
Training Epoch 6/10: 100% 26/26 [00:47<00:00,  1.84s/it]
Validation: 100% 3/3 [00:01<00:00,  1.72it/s]
Epoch 6/10, Train Loss: 0.0957, Validation Loss: 0.9329, Accuracy: 72.22%
Training Epoch 7/10: 100% 26/26 [00:47<00:00,  1.84s/it]
Validation: 100% 3/3 [00:01<00:00,  1.72it/s]
Epoch 7/10, Train Loss: 0.0476, Validation Loss: 1.0017, Accuracy: 72.22%
Early stopping triggered after epoch 7
=== BERTlarge - 5p training completed ===
```
