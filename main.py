def main():
    from torch_example import Net
    import torch
    model = Net()
    print(model(torch.randn(1, 1, 28, 28)))


if __name__ == "__main__":
    main()
