# Unit Test

The concept of unit testing is **Arrange, Act, Assert**.

- **Arrange:** Set up the conditions for the test and prepare any objects, variables, or data needed.

- **Act:** Call the function that you want to test.

- **Assert:** Check whether the output matches the expected result.

---

## Example

For `GTSRBDataset`, we can think about what the class is responsible for.



```coffeescript
class GTSRBDataset(Dataset):
    def __init__(
        self,
        manifest_path: str,
        transform=None,
    ):

        self.manifest = pd.read_csv(manifest_path)
        self.transform = transform

    def __len__(self):
        return len(self.manifest)

    def __getitem__(self, index):
        sample = self.manifest.iloc[index]

        img_path = sample["img_path"]
        label = int(sample["ClassId"])

        image = Image.open(img_path).convert("RGB")

        if self.transform is not None:
            image = self.transform(image)

        return image, label
```

```coffeescript
def test_dataset_length(
    tmp_path: Path,
):
    # Arrange
    manifest_path = tmp_path / "manifest.csv"
    pd.DataFrame(
        {
            "img_path": ["image_1.ppm"],
            "ClassId": [0],
        }
    ).to_csv(
        manifest_path,
        index=False,
    )

    # Act
    dataset = GTSRBDataset(
        manifest_path=manifest_path,
    )

    # Assert
    assert len(dataset) == 1

def test_dataset_returns_image_and_label(
    tmp_path: Path,
):

    # Arrange
    manifest_path = tmp_path / "manifest.csv"
    image_path = tmp_path / "image_1.ppm"
    pd.DataFrame(
        {
            "img_path": [str(image_path)],
            "ClassId": [1],
        }
    ).to_csv(
        manifest_path,
        index=False,
    )

    test_image = Image.new(
        mode="L",
        size=(20, 10),
    )

    test_image.save(image_path)

    # Act
    dataset = GTSRBDataset(
        manifest_path=manifest_path,
    )

    image, label = dataset[0]

    # Assert
    assert isinstance(image, Image.Image)
    assert image.mode == "RGB"
    assert image.size == (20, 10)
    assert label == 1
    assert isinstance(label, int)

```



The class mainly does two things:

- `__len__()`  returns the number of samples in the manifest.

- `__getitem__()`  load an image and returns the image and its label 

Therefore, we can write tests based on these behaviors.



> The goal of unit test can come from thinking about the behavior or responsibility of a function or a class 


