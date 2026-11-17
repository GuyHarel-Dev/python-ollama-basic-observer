import matplotlib.pyplot as plt
import numpy as np

from src.param_response_file_loader import ParamResponsesFilesLoader

class StatsPlotter:
    def __init__(self, title:str, x_data:list[float], y_data:list[float]):
       self.title = title
       self.x_data = x_data
       self.y_data = y_data



    def plot_bar_avg_std(self,size:tuple[float, float, str] = (15, 5, "in")): 
        
        plt.style.use("dark_background") 
        
        plt.figure(figsize=size)
        bars = plt.bar(self.x_data, self.y_data)
        plt.bar_label(# pyright: ignore[reportUnknownMemberType]   
            bars,
            padding= 3,  
            fontsize=8)
        plt.title(self.title)

        # Moyenne et écart-type
        moyenne = np.mean(self.y_data)
        ecart_type = np.std(self.y_data)

        # Lignes
        plt.axhline(
        moyenne,
        linestyle="--",
        linewidth=2,
        label=f"Moyenne : {moyenne:.1f} h"
        )

        plt.axhline(
        moyenne + ecart_type,
        linestyle=":",
        linewidth=1.5,
        label=f"+1 σ : {moyenne + ecart_type:.1f} h"
        )

        plt.axhline(
        moyenne - ecart_type,
        linestyle=":",
        linewidth=1.5,
        label=f"-1 σ : {moyenne - ecart_type:.1f} h"
        )

        plt.show()

        print(f"moy={moyenne}, std={ecart_type}")
