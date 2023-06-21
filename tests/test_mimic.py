import sys
from pathlib import Path

import pandas as pd

sys.path.append(str(Path(__file__).parent.parent / "pyAKI"))
from kdigo import Analyser, Dataset, DatasetType

if __name__ == "__main__":
    root_dir = Path(__file__).parent
    data_dir = root_dir / "data"

    urine_output = pd.read_csv(data_dir / "aki_urineoutput.csv")
    creatinine = pd.read_csv(data_dir / "aki_creatinine.csv")
    user_data = pd.DataFrame(
        data={
            "stay_id": urine_output["stay_id"].unique(),
            "weight": [100 for _ in range(20)],
        }
    )

    ana = Analyser(
        [
            Dataset(DatasetType.URINEOUTPUT, urine_output),
            Dataset(DatasetType.CREATININE, creatinine),
            Dataset(DatasetType.DEMOGRAPHICS, user_data),
        ]
    )
    ana.process_stays()