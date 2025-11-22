def aqi_calc(pm25=None, pm10=None, o3=None, no2=None, so2=None, co=None):
    """
    Calcula o AQI para múltiplos poluentes e determina o índice geral.
    Entrada: Valores de concentração em µg/m³.
    """

    def get_aqi(pollutant, c):
        if c is None or c < 0:
            return 0

        breakpoints = {
            "pm25": [
                (0, 12.0, 0, 50),
                (12.1, 35.4, 51, 100),
                (35.5, 55.4, 101, 150),
                (55.5, 150.4, 151, 200),
                (150.5, 250.4, 201, 300),
            ],
            "pm10": [
                (0, 54, 0, 50),
                (55, 154, 51, 100),
                (155, 254, 101, 150),
                (255, 354, 151, 200),
                (355, 424, 201, 300),
            ],
            "o3": [
                (0, 100, 0, 50),
                (101, 160, 51, 100),
                (161, 215, 101, 150),
                (216, 265, 151, 200),
            ],
            "no2": [
                (0, 100, 0, 50),
                (101, 189, 51, 100),
                (190, 677, 101, 150),
                (678, 1220, 151, 200),
            ],
            "so2": [
                (0, 92, 0, 50),
                (93, 196, 51, 100),
                (197, 484, 101, 150),
                (485, 797, 151, 200),
            ],
            "co": [
                (0, 5000, 0, 50),
                (5001, 10000, 51, 100),
                (10001, 14000, 101, 150),
            ],
        }

        bp = breakpoints.get(pollutant)
        if not bp:
            return 0

        for c_low, c_high, i_low, i_high in bp:
            if c_low <= c <= c_high:
                return round(
                    ((i_high - i_low) / (c_high - c_low)) * (c - c_low) + i_low
                )

        return 300

    resultados = {
        "PM2.5": get_aqi("pm25", pm25),
        "PM10": get_aqi("pm10", pm10),
        "O3": get_aqi("o3", o3),
        "NO2": get_aqi("no2", no2),
        "SO2": get_aqi("so2", so2),
        "CO": get_aqi("co", co),
    }

    return resultados


aqi_calc(co=140, no2=5.33, o3=83.23, pm10=2.23, pm25=2.18, so2=1.0)
