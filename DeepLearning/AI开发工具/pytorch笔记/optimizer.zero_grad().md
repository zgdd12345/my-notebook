<font style="color:rgb(18, 18, 18);">optimizer.zero_grad()意思是把梯度置零，也就是把loss关于weight的导数变成0。</font>

```python
# zero the parameter gradients
optimizer.zero_grad()  # 梯度初始化为零

# forward + backward + optimize
outputs = net(inputs)  # 前向传播求出预测的值

loss = criterion(outputs, labels) # 求loss

loss.backward()  # 反向传播求梯度

optimizer.step()  # 更新所有参数
```

 我们不需要将每一个patch数据的梯度积累起来，在计算下一个patch时需要清空上次计算的梯度。所以在每个patch开始的时候需要执行optimizer.zero_grad()

```python
# gradient descent
weights = [0] * n
alpha = 0.0001
max_Iter = 50000

for i in range(max_Iter):
    loss = 0
    d_weights = [0] * n  # 梯度初始化为零

    for k in range(m):
        h = dot(input[k], weights) # 前向传播求出预测的值

        # 反向传播求梯度
        d_weights = [d_weights[j] + (label[k] - h) * input[k][j] for j in range(n)] 
            
        loss += (label[k] - h) * (label[k] - h) / 2 # 求loss

    d_weights = [d_weights[k]/m for k in range(n)]

    # 更新所有参数
    weights = [weights[k] + alpha * d_weights[k] for k in range(n)]

    if i%10000 == 0:
        print "Iteration %d loss: %f"%(i, loss/m)
        print weights
```

