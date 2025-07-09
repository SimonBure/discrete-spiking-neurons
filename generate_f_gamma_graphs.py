import numpy as np
import matplotlib.pyplot as plt


# --- Constants ---
theta_max_potential = 0.5
beta_spike = 0.9
lambda_desactivation = 0.09

# --- Paramètres graphiques centralisés ---
PLOT_PARAMS = {
    'figsize': (8, 4),
    'xlabel': r'$\gamma$',
    'ylabel': r'$f(\gamma)$',
    'fontsize': 14,
    'title_fontsize': 16,
    'label_font': 'DejaVu Sans',
    'title_font': 'DejaVu Sans',
    'curve_color': 'blue',
    'grid': False,
    'xscale': 'linear',  # ou 'log' si besoin
    'ylim': None,        # exemple: (0, 5) si besoin
    'save_dir': '../rapport/figures/',
    'title': None        # Optionnel, peut être passé à plot_f_gamma
}

# --- Functions ---
def k_gamma(gamma):
    return np.ceil(theta_max_potential / gamma)


def f_gamma(gamma):
    return gamma - beta_spike * (
        1 / ((k_gamma(gamma) + 1 / beta_spike) * (beta_spike + lambda_desactivation))
    )

def plot_f_gamma(a, b, theta, filename, plot_params=None):
    if plot_params is None:
        plot_params = PLOT_PARAMS
    global theta_max_potential
    theta_max_potential = theta
    xs = np.linspace(a, b, 1000)
    ys = f_gamma(xs)
    plt.figure(figsize=plot_params['figsize'])
    plt.plot(xs, ys, color=plot_params.get('curve_color', 'blue'))
    plt.axhline(0, color='k', linewidth=0.7)
    plt.xlabel(plot_params['xlabel'], fontsize=plot_params['fontsize'], fontname=plot_params.get('label_font', None))
    plt.ylabel(plot_params['ylabel'], fontsize=plot_params['fontsize'], fontname=plot_params.get('label_font', None))
    plt.xscale(plot_params['xscale'])
    if plot_params['ylim'] is not None:
        plt.ylim(*plot_params['ylim'])
    if plot_params['grid']:
        plt.grid(True)
    if plot_params.get('title'):
        plt.title(plot_params['title'], fontsize=plot_params.get('title_fontsize', 16), fontname=plot_params.get('title_font', None))
    plt.tight_layout()
    plt.savefig(plot_params['save_dir'] + filename)
    plt.close()



if __name__ == "__main__":
    a, b = 1e-5, 1
    equilibrium_value = beta_spike / (
        (1 + 1 / beta_spike) * (beta_spike + lambda_desactivation)
    )
    print(f"Value of the equilibrium: {equilibrium_value}")
    print(
        f"For gamma in [{theta_max_potential}, {equilibrium_value}) f(gamma) is strictly negative."
    )
    print(f"For gamma in ({equilibrium_value}, 1] is strictly positive")

    # Pipeline pour générer les trois graphiques demandés
    plot_f_gamma(a, b, theta=3, filename="allure_f_gamma.png")
    plot_f_gamma(a, b, theta=0.2, filename="f_gamma_one_equilibre.png")
    plot_f_gamma(a, b, theta=0.5, filename="f_gamma_many_equilibres.png")
