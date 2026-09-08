# Unit Testing Inference with a Fake Model

For inference code, the unit testing approach is a little different.

The main goal is to check whether the prediction result is as expected.

Therefore, in the **Arrange** step, we first create a fake model with a controlled output.

Then, we use this fake model to verify that the logic inside the `predict()` function works correctly and returns the expected prediction.



```coffeescript
def predict(model: nn.Module, image: torch.Tensor, device: torch.device) -> int:

    image = image.unsqueeze(0)
    image = image.to(device)

    with torch.no_grad():
        outputs = model(image)
        prediction = torch.argmax(outputs, dim=1)

    return prediction.item()

```



```coffeescript
def test_predict():

    # arrange
    class FakeModel(nn.Module):
        def __init__(self):
            super().__init__()

        def forward(self, x):
            batch_size = x.shape[0]
            outputs = torch.zeros((batch_size, 43))
            outputs[:, 7] = 10
            return outputs

    fake_model = FakeModel()
    device = torch.device("cpu")
    fake_model.to(device)
    image = torch.randn(3, 32, 32)

    # act
    prediction = predict(fake_model, image, device)

    # assert
    assert prediction == 7
```

The fake model always assigns the highest score to class 7.

Therefore, if the `predict()` function works correctly, the returned prediction should be 7.


