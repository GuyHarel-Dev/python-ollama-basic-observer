from src.stats_plotter import StatsPlotter
from src.param_response_file_loader import ParamResponsesFilesLoader


class ResponseValuesPlotter:

    def plot_durations_bar_avg_std(
        self, file_loader: ParamResponsesFilesLoader, file_names: list[str]
    ):
        for file_name in file_names:
            file_name = file_name + ".jsonl"
            duration = file_loader.get_response_duration(file_name)

            y_data = duration.values
            x_data = [float(x) for x in list(range(len(y_data)))]

            plotter = StatsPlotter(
                "durations for:" + file_name, x_data=x_data, y_data=y_data
            )

            plotter.plot_bar_avg_std()
