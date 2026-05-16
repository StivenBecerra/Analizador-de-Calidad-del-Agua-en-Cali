import json

# GUARDAR RESUMEN EN JSON
def guardar_resumen_json(
    resumen,
    nombre_archivo="resumen_dataset.json"
):

    with open(
        nombre_archivo,
        "w",
        encoding="utf-8"
    ) as archivo:

        json.dump(
            resumen,
            archivo,
            indent=4,
            ensure_ascii=False
        )

    print(
        f"\nResumen guardado en {nombre_archivo}\n"
    )
