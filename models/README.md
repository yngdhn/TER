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

## DistilBERT

### 100p
```
```

### 10p
```
```

### 1p
```
```

## LargeBERT

### 100p
```
```

### 10p
```
```

### 1p
```
```