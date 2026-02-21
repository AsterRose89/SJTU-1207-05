import matplotlib.pyplot as plt

def plot_histogram(data, title, xlabel, ylabel, bins=50, save_path=None):
    """绘制频率分布直方图，支持保存图片"""
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=bins, density=True, alpha=0.7, color='skyblue', edgecolor='black')
    plt.title(title, fontsize=15)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()