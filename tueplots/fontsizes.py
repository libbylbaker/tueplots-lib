"""Fontsize settings."""

def icml():
    return from_base(base=10)

def neurips():
    return from_base(base=10)


def from_base(*, base=10):
    return {
        "axes.labelsize": base - 1,
        "font.size": base - 1,
        "legend.fontsize": base - 3,
        "xtick.labelsize": base - 3,
        "ytick.labelsize": base - 3,
    }