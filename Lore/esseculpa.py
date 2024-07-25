class Options:
    def __init__(self, fieldvar):
        self.fieldvar = fieldvar

opt = Options(fieldvar="some value")
fieldvar = opt.fieldvar
print(fieldvar)  # Output: "some value"
