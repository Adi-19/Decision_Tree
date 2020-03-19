import Node

data = [[]]
f = open('Soybean.csv')
for line in f:
	line = line.strip("\r\n")
	data.append(line.split(','))
data.remove([])
tree = {'date': {'october': {'plant-stand': {'lt-normal': {'precip': {'lt-norm': 'powdery-mildew', 'gt-norm': {'temp': {'lt-norm': 'downy-mildew', 'gt-norm': {'hail': {'yes': {'crop-hist': {'same-lst-yr': 'alternarialeaf-spot', 'same-lst-sev-yrs': {'area-damaged': {'whole-field': {'severity': {'minor': {'seed-tmt': {'fungicide': {'germination': {'lt-80': {'plant-growth': {'norm': {'leaves': {'abnorm': {'leafspots-halo': {'no-yellow-halos': {'leafspots-marg': {'w-s-marg': {'leafspot-size': {'gt-1/8': {'leaf-shread': {'absent': {'leaf-malf': {'absent': {'leaf-mild': {'absent': {'stem': {'abnorm': 'frog-eye-leaf-spot', 'norm': 'alternarialeaf-spot'}}}}}}}}}}}}}}}}}}}}}}}}, 'scattered': 'frog-eye-leaf-spot', 'upper-areas': 'alternarialeaf-spot', 'low-areas': 'frog-eye-leaf-spot'}}, 'same-lst-two-yrs': 'alternarialeaf-spot'}}, 'no': 'anthracnose'}}, 'norm': {'hail': {'yes': {'crop-hist': {'same-lst-yr': 'anthracnose', 'same-lst-sev-yrs': {'area-damaged': {'whole-field': 'anthracnose', 'upper-areas': 'frog-eye-leaf-spot'}}, 'same-lst-two-yrs': 'anthracnose'}}}}}}, 'norm': {'temp': {'lt-norm': 'powdery-mildew', 'gt-norm': 'alternarialeaf-spot', 'norm': 'brown-stem-rot'}}}}, 'normal': {'precip': {'lt-norm': {'temp': {'gt-norm': 'charcoal-rot', 'norm': {'hail': {'no': {'crop-hist': {'same-lst-yr': 'powdery-mildew', 'same-lst-two-yrs': 'brown-stem-rot', 'same-lst-sev-yrs': 'charcoal-rot'}}}}}}, 'gt-norm': {'temp': {'lt-norm': {'hail': {'yes': 'purple-seed-stain', 'no': {'crop-hist': {'same-lst-sev-yrs': 'purple-seed-stain', 'same-lst-two-yrs': {'area-damaged': {'upper-areas': 'purple-seed-stain', 'low-areas': 'downy-mildew'}}}}}}, 'gt-norm': {'hail': {'yes': {'crop-hist': {'same-lst-yr': {'area-damaged': {'whole-field': 'frog-eye-leaf-spot', 'scattered': 'alternarialeaf-spot', 'low-areas': 'frog-eye-leaf-spot'}}, 'same-lst-sev-yrs': 'alternarialeaf-spot', 'same-lst-two-yrs': {'area-damaged': {'scattered': {'severity': {'minor': {'seed-tmt': {'none': {'germination': {'80-89': {'plant-growth': {'norm': {'leaves': {'abnorm': {'leafspots-halo': {'no-yellow-halos': {'leafspots-marg': {'w-s-marg': {'leafspot-size': {'gt-1/8': {'leaf-shread': {'absent': {'leaf-malf': {'absent': {'leaf-mild': {'absent': {'stem': {'abnorm': 'frog-eye-leaf-spot', 'norm': 'alternarialeaf-spot'}}}}}}}}}}}}}}}}}}}}}}}}, 'low-areas': 'alternarialeaf-spot', 'upper-areas': {'severity': {'minor': {'seed-tmt': {'none': {'germination': {'80-89': {'plant-growth': {'norm': {'leaves': {'abnorm': {'leafspots-halo': {'no-yellow-halos': {'leafspots-marg': {'w-s-marg': {'leafspot-size': {'lt-1/8': 'purple-seed-stain', 'gt-1/8': 'alternarialeaf-spot'}}}}}}}}}}}}, 'fungicide': 'alternarialeaf-spot'}}}}}}}}}}, 'norm': {'hail': {'yes': {'crop-hist': {'diff-lst-year': 'alternarialeaf-spot', 'same-lst-yr': {'area-damaged': {'scattered': {'severity': {'pot-severe': 'diaporthe-stem-canker', 'minor': 'frog-eye-leaf-spot'}}, 'upper-areas': {'severity': {'minor': {'seed-tmt': {'none': 'frog-eye-leaf-spot', 'fungicide': 'alternarialeaf-spot'}}}}, 'low-areas': {'severity': {'pot-severe': {'seed-tmt': {'none': 'diaporthe-stem-canker', 'fungicide': 'anthracnose'}}, 'minor': 'alternarialeaf-spot'}}}}, 'same-lst-sev-yrs': {'area-damaged': {'whole-field': {'severity': {'pot-severe': 'anthracnose', 'minor': {'seed-tmt': {'fungicide': {'germination': {'lt-80': 'purple-seed-stain', '80-89': 'alternarialeaf-spot', '90-100': 'alternarialeaf-spot'}}}}}}, 'scattered': 'diaporthe-stem-canker'}}, 'same-lst-two-yrs': {'area-damaged': {'scattered': 'diaporthe-stem-canker', 'low-areas': 'alternarialeaf-spot', 'upper-areas': {'severity': {'pot-severe': 'anthracnose', 'minor': {'seed-tmt': {'none': {'germination': {'lt-80': 'purple-seed-stain', '90-100': 'anthracnose'}}}}}}}}}}}}}}, 'norm': {'temp': {'lt-norm': 'powdery-mildew', 'gt-norm': {'hail': {'yes': 'frog-eye-leaf-spot', 'no': 'alternarialeaf-spot'}}, 'norm': {'hail': {'yes': {'crop-hist': {'same-lst-two-yrs': 'frog-eye-leaf-spot', 'same-lst-sev-yrs': 'alternarialeaf-spot'}}, 'no': {'crop-hist': {'diff-lst-year': 'alternarialeaf-spot', 'same-lst-two-yrs': {'area-damaged': {'scattered': 'brown-stem-rot', 'upper-areas': 'alternarialeaf-spot'}}}}}}}}}}}}, 'august': {'plant-stand': {'lt-normal': {'precip': {'lt-norm': 'brown-stem-rot', 'gt-norm': {'temp': {'lt-norm': 'downy-mildew', 'gt-norm': {'hail': {'yes': {'crop-hist': {'diff-lst-year': 'alternarialeaf-spot', 'same-lst-two-yrs': 'downy-mildew'}}, 'no': {'crop-hist': {'same-lst-yr': 'anthracnose', 'same-lst-sev-yrs': 'frog-eye-leaf-spot', 'same-lst-two-yrs': {'area-damaged': {'upper-areas': 'anthracnose', 'low-areas': 'bacterial-blight'}}}}}}, 'norm': {'hail': {'yes': {'crop-hist': {'diff-lst-year': 'alternarialeaf-spot', 'same-lst-yr': {'area-damaged': {'upper-areas': 'alternarialeaf-spot', 'low-areas': {'severity': {'severe': 'anthracnose', 'pot-severe': 'alternarialeaf-spot'}}}}, 'same-lst-two-yrs': {'area-damaged': {'upper-areas': 'alternarialeaf-spot', 'low-areas': {'severity': {'minor': {'seed-tmt': {'none': 'alternarialeaf-spot', 'fungicide': 'frog-eye-leaf-spot'}}}}}}, 'same-lst-sev-yrs': {'area-damaged': {'whole-field': 'brown-spot', 'scattered': {'severity': {'pot-severe': {'seed-tmt': {'none': {'germination': {'lt-80': {'plant-growth': {'norm': {'leaves': {'abnorm': {'leafspots-halo': {'yellow-halos': 'bacterial-pustule', 'no-yellow-halos': 'frog-eye-leaf-spot'}}}}}}}}, 'fungicide': 'alternarialeaf-spot'}}}}, 'upper-areas': {'severity': {'pot-severe': {'seed-tmt': {'none': {'germination': {'lt-80': {'plant-growth': {'norm': {'leaves': {'abnorm': {'leafspots-halo': {'no-yellow-halos': {'leafspots-marg': {'w-s-marg': {'leafspot-size': {'gt-1/8': {'leaf-shread': {'absent': {'leaf-malf': {'absent': {'leaf-mild': {'absent': {'stem': {'abnorm': 'frog-eye-leaf-spot', 'norm': 'alternarialeaf-spot'}}}}}}}}}}}}}}}}}}}}}}}}, 'low-areas': {'severity': {'pot-severe': {'seed-tmt': {'none': 'brown-spot', 'fungicide': {'germination': {'lt-80': {'plant-growth': {'norm': {'leaves': {'abnorm': {'leafspots-halo': {'no-yellow-halos': {'leafspots-marg': {'w-s-marg': {'leafspot-size': {'gt-1/8': {'leaf-shread': {'absent': {'leaf-malf': {'absent': {'leaf-mild': {'absent': {'stem': {'norm': {'lodging': {'yes': {'stem-cankers': {'absent': {'canker-lesion': {'dna': {'fruiting-bodies': {'absent': {'external-decay': {'absent': {'mycelium': {'absent': {'int-discolor': {'none': {'sclerotia': {'absent': {'fruit-pods': {'norm': {'fruit-spots': {'absent': {'seed': {'norm': {'mold-growth': {'absent': {'seed-discolor': {'absent': {'seed-size': {'norm': {'shriveling': {'absent': {'roots': {'norm': 'alternarialeaf-spot'}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}, 'norm': {'temp': {'lt-norm': {'hail': {'yes': {'crop-hist': {'diff-lst-year': 'powdery-mildew', 'same-lst-sev-yrs': 'brown-stem-rot', 'same-lst-two-yrs': 'powdery-mildew'}}}}, 'gt-norm': {'hail': {'yes': {'crop-hist': {'same-lst-yr': {'area-damaged': {'whole-field': 'phyllosticta-leaf-spot', 'upper-areas': 'phyllosticta-leaf-spot', 'low-areas': 'frog-eye-leaf-spot'}}}}}}, 'norm': {'hail': {'yes': 'bacterial-blight', 'no': 'brown-spot'}}}}}}, 'normal': {'precip': {'lt-norm': {'temp': {'gt-norm': 'charcoal-rot', 'norm': {'hail': {'yes': {'crop-hist': {'same-lst-yr': 'brown-stem-rot', 'same-lst-sev-yrs': 'brown-stem-rot', 'same-lst-two-yrs': {'area-damaged': {'whole-field': 'charcoal-rot', 'scattered': 'brown-stem-rot', 'upper-areas': 'charcoal-rot'}}}}, 'no': {'crop-hist': {'same-lst-yr': 'charcoal-rot', 'same-lst-sev-yrs': 'powdery-mildew'}}}}}}, 'gt-norm': {'temp': {'lt-norm': {'hail': {'yes': 'purple-seed-stain', 'no': 'rhizoctonia-root-rot'}}, 'gt-norm': {'hail': {'yes': {'crop-hist': {'same-lst-yr': {'area-damaged': {'whole-field': 'frog-eye-leaf-spot', 'scattered': 'frog-eye-leaf-spot', 'upper-areas': 'frog-eye-leaf-spot', 'low-areas': {'severity': {'pot-severe': {'seed-tmt': {'none': 'alternarialeaf-spot', 'fungicide': 'frog-eye-leaf-spot'}}}}}}, 'same-lst-two-yrs': 'frog-eye-leaf-spot', 'same-lst-sev-yrs': 'alternarialeaf-spot'}}, 'no': {'crop-hist': {'diff-lst-year': 'purple-seed-stain', 'same-lst-yr': 'frog-eye-leaf-spot', 'same-lst-sev-yrs': 'frog-eye-leaf-spot', 'same-lst-two-yrs': 'bacterial-blight'}}}}, 'norm': {'hail': {'yes': {'crop-hist': {'diff-lst-year': {'area-damaged': {'scattered': {'severity': {'minor': {'seed-tmt': {'fungicide': {'germination': {'80-89': {'plant-growth': {'norm': {'leaves': {'abnorm': 'anthracnose', 'norm': 'purple-seed-stain'}}}}}}}}}}, 'low-areas': 'frog-eye-leaf-spot'}}, 'same-lst-yr': {'area-damaged': {'whole-field': {'severity': {'pot-severe': {'seed-tmt': {'none': 'brown-spot', 'fungicide': 'frog-eye-leaf-spot'}}}}, 'scattered': {'severity': {'pot-severe': {'seed-tmt': {'none': {'germination': {'90-100': {'plant-growth': {'norm': {'leaves': {'abnorm': {'leafspots-halo': {'no-yellow-halos': {'leafspots-marg': {'w-s-marg': {'leafspot-size': {'gt-1/8': {'leaf-shread': {'absent': {'leaf-malf': {'absent': {'leaf-mild': {'absent': {'stem': {'abnorm': 'frog-eye-leaf-spot', 'norm': 'alternarialeaf-spot'}}}}}}}}}}}}}}}}}}}}}}}}, 'upper-areas': {'severity': {'pot-severe': {'seed-tmt': {'none': {'germination': {'80-89': 'frog-eye-leaf-spot', '90-100': {'plant-growth': {'norm': {'leaves': {'abnorm': {'leafspots-halo': {'no-yellow-halos': {'leafspots-marg': {'w-s-marg': {'leafspot-size': {'gt-1/8': {'leaf-shread': {'absent': {'leaf-malf': {'absent': {'leaf-mild': {'absent': {'stem': {'abnorm': 'frog-eye-leaf-spot', 'norm': 'alternarialeaf-spot'}}}}}}}}}}}}}}}}}}}}}}}}, 'low-areas': {'severity': {'severe': 'anthracnose', 'pot-severe': 'alternarialeaf-spot'}}}}, 'same-lst-sev-yrs': {'area-damaged': {'whole-field': 'brown-spot', 'scattered': 'diaporthe-stem-canker'}}, 'same-lst-two-yrs': {'area-damaged': {'whole-field': {'severity': {'severe': 'brown-spot', 'pot-severe': 'frog-eye-leaf-spot', 'minor': 'frog-eye-leaf-spot'}}, 'scattered': {'severity': {'severe': 'diaporthe-stem-canker', 'pot-severe': 'frog-eye-leaf-spot', 'minor': 'frog-eye-leaf-spot'}}, 'low-areas': {'severity': {'pot-severe': {'seed-tmt': {'none': 'brown-spot', 'fungicide': 'frog-eye-leaf-spot'}}}}, 'upper-areas': {'severity': {'pot-severe': {'seed-tmt': {'none': {'germination': {'80-89': {'plant-growth': {'norm': {'leaves': {'abnorm': {'leafspots-halo': {'no-yellow-halos': {'leafspots-marg': {'w-s-marg': {'leafspot-size': {'gt-1/8': {'leaf-shread': {'absent': {'leaf-malf': {'absent': {'leaf-mild': {'absent': {'stem': {'abnorm': 'frog-eye-leaf-spot', 'norm': 'alternarialeaf-spot'}}}}}}}}}}}}}}}}}}}}, 'fungicide': 'anthracnose'}}, 'minor': 'alternarialeaf-spot'}}}}}}, 'no': {'crop-hist': {'diff-lst-year': {'area-damaged': {'whole-field': 'bacterial-blight', 'scattered': {'severity': {'pot-severe': 'alternarialeaf-spot', 'minor': 'purple-seed-stain'}}}}, 'same-lst-yr': {'area-damaged': {'scattered': 'diaporthe-stem-canker', 'low-areas': 'purple-seed-stain'}}, 'same-lst-sev-yrs': {'area-damaged': {'whole-field': 'downy-mildew', 'low-areas': 'bacterial-blight'}}}}}}}}, 'norm': {'temp': {'lt-norm': {'hail': {'no': {'crop-hist': {'same-lst-sev-yrs': 'brown-stem-rot', 'same-lst-two-yrs': {'area-damaged': {'whole-field': 'brown-stem-rot', 'upper-areas': {'severity': {'pot-severe': 'brown-stem-rot', 'minor': 'powdery-mildew'}}}}}}}}, 'gt-norm': {'hail': {'yes': {'crop-hist': {'same-lst-yr': 'frog-eye-leaf-spot', 'same-lst-sev-yrs': 'bacterial-blight'}}}}, 'norm': {'hail': {'yes': {'crop-hist': {'same-lst-yr': 'brown-spot', 'same-lst-sev-yrs': {'area-damaged': {'whole-field': {'severity': {'pot-severe': {'seed-tmt': {'none': 'alternarialeaf-spot', 'fungicide': 'frog-eye-leaf-spot'}}}}}}}}, 'no': {'crop-hist': {'same-lst-yr': 'bacterial-pustule', 'same-lst-sev-yrs': 'frog-eye-leaf-spot'}}}}}}}}}}, 'april': {'plant-stand': {'lt-normal': {'precip': {'gt-norm': {'temp': {'lt-norm': 'rhizoctonia-root-rot', 'gt-norm': 'brown-spot', 'norm': 'phytophthora-rot'}}, 'norm': {'temp': {'norm': {'hail': {'yes': 'phytophthora-rot', 'no': {'crop-hist': {'same-lst-two-yrs': {'area-damaged': {'upper-areas': 'brown-spot', 'low-areas': 'phytophthora-rot'}}}}}}}}}}, 'normal': {'precip': {'gt-norm': {'temp': {'gt-norm': 'brown-spot', 'norm': 'anthracnose'}}, 'norm': 'brown-spot'}}}}, 'september': {'plant-stand': {'lt-normal': {'precip': {'lt-norm': {'temp': {'lt-norm': 'brown-stem-rot', 'norm': {'hail': {'yes': {'crop-hist': {'same-lst-yr': {'area-damaged': {'whole-field': 'brown-stem-rot', 'low-areas': 'powdery-mildew'}}, 'same-lst-sev-yrs': 'powdery-mildew'}}}}}}, 'gt-norm': {'temp': {'lt-norm': 'downy-mildew', 'gt-norm': {'hail': {'yes': {'crop-hist': {'same-lst-two-yrs': 'alternarialeaf-spot', 'same-lst-sev-yrs': {'area-damaged': {'whole-field': {'severity': {'pot-severe': 'alternarialeaf-spot', 'minor': {'seed-tmt': {'fungicide': {'germination': {'lt-80': {'plant-growth': {'norm': {'leaves': {'abnorm': {'leafspots-halo': {'no-yellow-halos': {'leafspots-marg': {'w-s-marg': {'leafspot-size': {'gt-1/8': {'leaf-shread': {'absent': {'leaf-malf': {'absent': {'leaf-mild': {'absent': {'stem': {'abnorm': 'frog-eye-leaf-spot', 'norm': 'alternarialeaf-spot'}}}}}}}}}}}}}}}}}}}}}}}}, 'scattered': 'alternarialeaf-spot', 'upper-areas': 'alternarialeaf-spot', 'low-areas': {'severity': {'pot-severe': 'alternarialeaf-spot', 'minor': {'seed-tmt': {'none': 'alternarialeaf-spot', 'fungicide': {'germination': {'lt-80': {'plant-growth': {'norm': {'leaves': {'abnorm': {'leafspots-halo': {'no-yellow-halos': {'leafspots-marg': {'w-s-marg': {'leafspot-size': {'gt-1/8': {'leaf-shread': {'absent': {'leaf-malf': {'absent': {'leaf-mild': {'absent': {'stem': {'abnorm': 'frog-eye-leaf-spot', 'norm': 'alternarialeaf-spot'}}}}}}}}}}}}}}}}}}}}}}}}}}}}, 'no': 'anthracnose'}}, 'norm': {'hail': {'yes': {'crop-hist': {'diff-lst-year': 'alternarialeaf-spot', 'same-lst-yr': {'area-damaged': {'upper-areas': 'frog-eye-leaf-spot', 'low-areas': 'anthracnose'}}, 'same-lst-two-yrs': {'area-damaged': {'whole-field': {'severity': {'minor': {'seed-tmt': {'fungicide': {'germination': {'lt-80': {'plant-growth': {'norm': {'leaves': {'abnorm': {'leafspots-halo': {'yellow-halos': 'downy-mildew', 'no-yellow-halos': 'frog-eye-leaf-spot'}}}}}}}}}}}}, 'upper-areas': {'severity': {'pot-severe': 'anthracnose', 'minor': 'alternarialeaf-spot'}}}}, 'same-lst-sev-yrs': {'area-damaged': {'whole-field': {'severity': {'severe': 'brown-spot', 'pot-severe': {'seed-tmt': {'none': {'germination': {'lt-80': 'brown-spot', '80-89': 'anthracnose'}}, 'fungicide': 'anthracnose'}}, 'minor': {'seed-tmt': {'fungicide': {'germination': {'lt-80': {'plant-growth': {'norm': {'leaves': {'abnorm': {'leafspots-halo': {'no-yellow-halos': {'leafspots-marg': {'w-s-marg': {'leafspot-size': {'gt-1/8': {'leaf-shread': {'absent': 'frog-eye-leaf-spot', 'present': 'alternarialeaf-spot'}}}}}}}}}}}}}}}}}}, 'scattered': 'frog-eye-leaf-spot', 'upper-areas': {'severity': {'pot-severe': 'downy-mildew', 'minor': 'frog-eye-leaf-spot'}}}}}}, 'no': {'crop-hist': {'diff-lst-year': 'alternarialeaf-spot', 'same-lst-yr': {'area-damaged': {'whole-field': 'bacterial-blight', 'low-areas': 'alternarialeaf-spot'}}}}}}}}, 'norm': {'temp': {'lt-norm': 'brown-stem-rot', 'gt-norm': 'alternarialeaf-spot', 'norm': {'hail': {'yes': {'crop-hist': {'same-lst-two-yrs': {'area-damaged': {'whole-field': 'brown-stem-rot', 'scattered': 'bacterial-pustule'}}}}}}}}}}, 'normal': {'precip': {'lt-norm': {'temp': {'gt-norm': {'hail': {'yes': {'crop-hist': {'diff-lst-year': 'charcoal-rot', 'same-lst-yr': 'brown-stem-rot', 'same-lst-sev-yrs': {'area-damaged': {'scattered': 'brown-stem-rot', 'upper-areas': {'severity': {'pot-severe': {'seed-tmt': {'none': 'charcoal-rot', 'fungicide': 'brown-stem-rot'}}}}}}, 'same-lst-two-yrs': 'brown-stem-rot'}}, 'no': 'charcoal-rot'}}, 'norm': {'hail': {'yes': 'brown-stem-rot', 'no': {'crop-hist': {'same-lst-sev-yrs': {'area-damaged': {'whole-field': {'severity': {'pot-severe': {'seed-tmt': {'none': {'germination': {'lt-80': 'brown-stem-rot', '80-89': 'powdery-mildew'}}}}}}, 'scattered': 'brown-stem-rot'}}}}}}}}, 'gt-norm': {'temp': {'lt-norm': 'purple-seed-stain', 'gt-norm': {'hail': {'yes': {'crop-hist': {'same-lst-yr': {'area-damaged': {'whole-field': {'severity': {'pot-severe': 'alternarialeaf-spot', 'minor': {'seed-tmt': {'fungicide': {'germination': {'90-100': {'plant-growth': {'norm': {'leaves': {'abnorm': {'leafspots-halo': {'no-yellow-halos': {'leafspots-marg': {'w-s-marg': {'leafspot-size': {'gt-1/8': {'leaf-shread': {'absent': {'leaf-malf': {'absent': {'leaf-mild': {'absent': {'stem': {'abnorm': 'frog-eye-leaf-spot', 'norm': 'alternarialeaf-spot'}}}}}}}}}}}}}}}}}}}}}}}}, 'scattered': 'alternarialeaf-spot', 'low-areas': {'severity': {'pot-severe': 'alternarialeaf-spot', 'minor': {'seed-tmt': {'fungicide': {'germination': {'lt-80': 'purple-seed-stain', '80-89': 'alternarialeaf-spot', '90-100': {'plant-growth': {'norm': {'leaves': {'abnorm': {'leafspots-halo': {'no-yellow-halos': {'leafspots-marg': {'w-s-marg': {'leafspot-size': {'gt-1/8': {'leaf-shread': {'absent': {'leaf-malf': {'absent': {'leaf-mild': {'absent': {'stem': {'abnorm': 'frog-eye-leaf-spot', 'norm': 'alternarialeaf-spot'}}}}}}}}}}}}}}}}}}}}}}}}}}, 'same-lst-two-yrs': {'area-damaged': {'whole-field': {'severity': {'pot-severe': 'alternarialeaf-spot', 'minor': {'seed-tmt': {'none': 'alternarialeaf-spot', 'fungicide': {'germination': {'80-89': {'plant-growth': {'norm': {'leaves': {'abnorm': {'leafspots-halo': {'no-yellow-halos': {'leafspots-marg': {'w-s-marg': {'leafspot-size': {'gt-1/8': {'leaf-shread': {'absent': {'leaf-malf': {'absent': {'leaf-mild': {'absent': {'stem': {'abnorm': 'frog-eye-leaf-spot', 'norm': 'alternarialeaf-spot'}}}}}}}}}}}}}}}}}}}}}}}}, 'scattered': {'severity': {'pot-severe': 'alternarialeaf-spot', 'minor': 'frog-eye-leaf-spot'}}, 'low-areas': {'severity': {'pot-severe': 'alternarialeaf-spot', 'minor': 'frog-eye-leaf-spot'}}, 'upper-areas': {'severity': {'pot-severe': 'alternarialeaf-spot', 'minor': 'frog-eye-leaf-spot'}}}}, 'same-lst-sev-yrs': 'alternarialeaf-spot'}}, 'no': 'purple-seed-stain'}}, 'norm': {'hail': {'yes': {'crop-hist': {'diff-lst-year': {'area-damaged': {'whole-field': 'alternarialeaf-spot', 'low-areas': 'frog-eye-leaf-spot'}}, 'same-lst-yr': {'area-damaged': {'whole-field': 'brown-spot', 'scattered': 'diaporthe-stem-canker', 'upper-areas': {'severity': {'pot-severe': 'brown-spot', 'minor': {'seed-tmt': {'none': 'frog-eye-leaf-spot', 'fungicide': 'alternarialeaf-spot'}}}}, 'low-areas': {'severity': {'pot-severe': {'seed-tmt': {'none': 'anthracnose', 'other': 'anthracnose', 'fungicide': 'frog-eye-leaf-spot'}}, 'minor': 'purple-seed-stain'}}}}, 'same-lst-two-yrs': {'area-damaged': {'whole-field': {'severity': {'severe': 'brown-spot', 'minor': 'frog-eye-leaf-spot'}}, 'scattered': {'severity': {'pot-severe': 'diaporthe-stem-canker', 'minor': 'frog-eye-leaf-spot'}}, 'low-areas': 'alternarialeaf-spot', 'upper-areas': {'severity': {'pot-severe': {'seed-tmt': {'none': {'germination': {'lt-80': 'anthracnose', '80-89': 'brown-spot', '90-100': 'anthracnose'}}}}, 'minor': 'alternarialeaf-spot'}}}}, 'same-lst-sev-yrs': {'area-damaged': {'whole-field': 'anthracnose', 'scattered': {'severity': {'pot-severe': {'seed-tmt': {'none': {'germination': {'80-89': {'plant-growth': {'abnorm': 'diaporthe-stem-canker', 'norm': 'frog-eye-leaf-spot'}}, '90-100': 'frog-eye-leaf-spot'}}}}, 'minor': 'alternarialeaf-spot'}}, 'low-areas': 'diaporthe-stem-canker', 'upper-areas': {'severity': {'pot-severe': {'seed-tmt': {'none': {'germination': {'80-89': 'brown-spot', '90-100': 'frog-eye-leaf-spot'}}}}}}}}}}, 'no': {'crop-hist': {'same-lst-yr': 'downy-mildew', 'same-lst-two-yrs': {'area-damaged': {'upper-areas': {'severity': {'pot-severe': 'alternarialeaf-spot', 'minor': 'frog-eye-leaf-spot'}}}}, 'same-lst-sev-yrs': 'bacterial-blight'}}}}}}, 'norm': {'temp': {'lt-norm': 'powdery-mildew', 'gt-norm': 'bacterial-pustule', 'norm': 'frog-eye-leaf-spot'}}}}}}, 'june': {'plant-stand': {'lt-normal': {'precip': {'gt-norm': {'temp': {'lt-norm': {'hail': {'yes': {'crop-hist': {'diff-lst-year': 'rhizoctonia-root-rot', 'same-lst-yr': {'area-damaged': {'upper-areas': 'bacterial-pustule', 'low-areas': {'severity': {'severe': {'seed-tmt': {'none': {'germination': {'lt-80': 'rhizoctonia-root-rot', '80-89': 'phytophthora-rot', '90-100': 'phytophthora-rot'}}}}}}}}, 'same-lst-sev-yrs': {'area-damaged': {'scattered': 'downy-mildew', 'low-areas': 'rhizoctonia-root-rot'}}, 'same-lst-two-yrs': 'rhizoctonia-root-rot'}}}}, 'gt-norm': {'hail': {'yes': 'bacterial-pustule', 'no': {'crop-hist': {'diff-lst-year': 'anthracnose', 'same-lst-sev-yrs': 'brown-spot'}}}}, 'norm': {'hail': {'yes': {'crop-hist': {'same-lst-sev-yrs': 'brown-spot', 'same-lst-two-yrs': {'area-damaged': {'whole-field': 'brown-spot', 'scattered': 'downy-mildew'}}}}, 'no': 'phytophthora-rot'}}}}, 'norm': {'temp': {'lt-norm': {'hail': {'yes': {'crop-hist': {'diff-lst-year': 'powdery-mildew', 'same-lst-sev-yrs': 'phytophthora-rot', 'same-lst-two-yrs': 'powdery-mildew'}}}}, 'gt-norm': {'hail': {'yes': {'crop-hist': {'same-lst-sev-yrs': 'phyllosticta-leaf-spot', 'same-lst-two-yrs': 'bacterial-pustule'}}}}, 'norm': {'hail': {'yes': {'crop-hist': {'same-lst-yr': 'bacterial-blight', 'same-lst-two-yrs': 'phyllosticta-leaf-spot'}}, 'no': 'brown-spot'}}}}}}, 'normal': {'precip': {'lt-norm': 'phyllosticta-leaf-spot', 'gt-norm': {'temp': {'lt-norm': 'downy-mildew', 'gt-norm': 'brown-spot', 'norm': {'hail': {'yes': {'crop-hist': {'same-lst-yr': 'brown-spot', 'same-lst-sev-yrs': 'brown-spot', 'same-lst-two-yrs': {'area-damaged': {'whole-field': 'brown-spot', 'upper-areas': {'severity': {'pot-severe': 'brown-spot', 'minor': 'anthracnose'}}}}}}, 'no': {'crop-hist': {'same-lst-yr': {'area-damaged': {'whole-field': 'bacterial-pustule', 'low-areas': 'downy-mildew'}}, 'same-lst-sev-yrs': 'bacterial-pustule'}}}}}}, 'norm': {'temp': {'lt-norm': 'bacterial-pustule', 'gt-norm': 'bacterial-pustule', 'norm': {'hail': {'yes': {'crop-hist': {'diff-lst-year': 'bacterial-blight', 'same-lst-two-yrs': 'brown-spot', 'same-lst-sev-yrs': 'bacterial-blight'}}, 'no': 'powdery-mildew'}}}}}}}}, 'may': {'plant-stand': {'lt-normal': {'precip': {'lt-norm': 'powdery-mildew', 'gt-norm': {'temp': {'lt-norm': {'hail': {'yes': {'crop-hist': {'diff-lst-year': {'area-damaged': {'low-areas': {'severity': {'severe': 'phytophthora-rot', 'pot-severe': 'rhizoctonia-root-rot'}}}}, 'same-lst-yr': 'rhizoctonia-root-rot', 'same-lst-sev-yrs': {'area-damaged': {'low-areas': {'severity': {'severe': 'rhizoctonia-root-rot', 'pot-severe': 'phytophthora-rot'}}}}, 'same-lst-two-yrs': {'area-damaged': {'low-areas': {'severity': {'severe': {'seed-tmt': {'none': 'rhizoctonia-root-rot', 'fungicide': 'phytophthora-rot'}}, 'pot-severe': 'rhizoctonia-root-rot'}}}}}}}}, 'gt-norm': 'brown-spot', 'norm': {'hail': {'yes': {'crop-hist': {'diff-lst-year': 'phytophthora-rot', 'same-lst-yr': 'brown-spot', 'same-lst-sev-yrs': 'brown-spot', 'same-lst-two-yrs': 'brown-spot'}}, 'no': 'phytophthora-rot'}}}}, 'norm': {'temp': {'norm': {'hail': {'yes': {'crop-hist': {'same-lst-yr': 'bacterial-pustule', 'same-lst-two-yrs': 'phyllosticta-leaf-spot'}}, 'no': 'brown-spot'}}}}}}, 'normal': {'precip': {'lt-norm': {'temp': {'lt-norm': 'powdery-mildew', 'gt-norm': 'phyllosticta-leaf-spot', 'norm': 'phyllosticta-leaf-spot'}}, 'gt-norm': {'temp': {'lt-norm': 'downy-mildew', 'gt-norm': 'brown-spot', 'norm': {'hail': {'yes': {'crop-hist': {'diff-lst-year': 'anthracnose', 'same-lst-yr': {'area-damaged': {'whole-field': 'brown-spot', 'low-areas': {'severity': {'pot-severe': {'seed-tmt': {'none': 'brown-spot', 'fungicide': 'anthracnose'}}}}}}, 'same-lst-sev-yrs': 'brown-spot', 'same-lst-two-yrs': 'brown-spot'}}, 'no': 'downy-mildew'}}}}, 'norm': {'temp': {'norm': {'hail': {'yes': 'brown-spot', 'no': 'bacterial-pustule'}}}}}}}}, 'july': {'plant-stand': {'lt-normal': {'precip': {'lt-norm': {'temp': {'lt-norm': 'brown-stem-rot', 'norm': 'powdery-mildew'}}, 'gt-norm': {'temp': {'lt-norm': 'phytophthora-rot', 'gt-norm': {'hail': {'yes': 'downy-mildew', 'no': {'crop-hist': {'same-lst-yr': {'area-damaged': {'low-areas': {'severity': {'minor': {'seed-tmt': {'other': 'brown-spot', 'fungicide': 'anthracnose'}}}}}}, 'same-lst-two-yrs': 'frog-eye-leaf-spot'}}}}, 'norm': {'hail': {'yes': {'crop-hist': {'diff-lst-year': 'bacterial-pustule', 'same-lst-yr': {'area-damaged': {'whole-field': 'brown-spot', 'low-areas': 'downy-mildew'}}, 'same-lst-sev-yrs': {'area-damaged': {'whole-field': 'brown-spot', 'scattered': 'frog-eye-leaf-spot', 'upper-areas': 'frog-eye-leaf-spot', 'low-areas': {'severity': {'pot-severe': {'seed-tmt': {'none': 'brown-spot', 'fungicide': 'frog-eye-leaf-spot'}}}}}}}}, 'no': 'frog-eye-leaf-spot'}}}}, 'norm': {'temp': {'lt-norm': {'hail': {'yes': {'crop-hist': {'same-lst-two-yrs': {'area-damaged': {'scattered': {'severity': {'severe': 'brown-stem-rot', 'minor': 'bacterial-pustule'}}, 'low-areas': 'phytophthora-rot'}}}}}}, 'gt-norm': 'phyllosticta-leaf-spot', 'norm': {'hail': {'yes': {'crop-hist': {'diff-lst-year': 'phyllosticta-leaf-spot', 'same-lst-sev-yrs': 'bacterial-pustule'}}}}}}}}, 'normal': {'precip': {'lt-norm': {'temp': {'lt-norm': 'brown-stem-rot', 'gt-norm': 'charcoal-rot', 'norm': {'hail': {'yes': {'crop-hist': {'same-lst-yr': 'charcoal-rot', 'same-lst-two-yrs': 'brown-stem-rot', 'same-lst-sev-yrs': 'brown-stem-rot'}}, 'no': 'phyllosticta-leaf-spot'}}}}, 'gt-norm': {'temp': {'lt-norm': {'hail': {'yes': 'purple-seed-stain', 'no': {'crop-hist': {'diff-lst-year': 'purple-seed-stain', 'same-lst-two-yrs': {'area-damaged': {'whole-field': 'bacterial-pustule', 'upper-areas': {'severity': {'pot-severe': 'downy-mildew', 'minor': 'powdery-mildew'}}}}, 'same-lst-sev-yrs': 'rhizoctonia-root-rot'}}}}, 'gt-norm': {'hail': {'yes': {'crop-hist': {'same-lst-two-yrs': 'frog-eye-leaf-spot', 'same-lst-sev-yrs': {'area-damaged': {'whole-field': {'severity': {'minor': {'seed-tmt': {'none': {'germination': {'80-89': {'plant-growth': {'abnorm': 'brown-spot', 'norm': 'purple-seed-stain'}}}}}}}}}}}}}}, 'norm': {'hail': {'yes': {'crop-hist': {'diff-lst-year': 'alternarialeaf-spot', 'same-lst-yr': {'area-damaged': {'scattered': {'severity': {'severe': 'diaporthe-stem-canker', 'pot-severe': 'frog-eye-leaf-spot'}}, 'low-areas': 'frog-eye-leaf-spot', 'upper-areas': 'frog-eye-leaf-spot'}}, 'same-lst-sev-yrs': {'area-damaged': {'whole-field': {'severity': {'severe': 'brown-spot', 'pot-severe': {'seed-tmt': {'none': {'germination': {'80-89': 'brown-spot', '90-100': 'anthracnose'}}}}}}, 'scattered': 'diaporthe-stem-canker', 'low-areas': 'brown-spot'}}, 'same-lst-two-yrs': {'area-damaged': {'whole-field': {'severity': {'severe': 'brown-spot', 'pot-severe': 'brown-spot', 'minor': 'frog-eye-leaf-spot'}}, 'scattered': 'diaporthe-stem-canker', 'upper-areas': 'brown-spot', 'low-areas': {'severity': {'pot-severe': {'seed-tmt': {'none': {'germination': {'80-89': 'diaporthe-stem-canker', '90-100': 'brown-spot'}}, 'fungicide': 'alternarialeaf-spot'}}}}}}}}, 'no': {'crop-hist': {'diff-lst-year': 'frog-eye-leaf-spot', 'same-lst-yr': {'area-damaged': {'scattered': 'downy-mildew', 'upper-areas': 'bacterial-blight', 'low-areas': {'severity': {'pot-severe': {'seed-tmt': {'none': 'bacterial-pustule', 'fungicide': 'bacterial-blight'}}}}}}, 'same-lst-sev-yrs': 'purple-seed-stain', 'same-lst-two-yrs': 'bacterial-blight'}}}}}}, 'norm': {'temp': {'lt-norm': 'bacterial-pustule', 'norm': {'hail': {'yes': 'bacterial-blight', 'no': 'bacterial-pustule'}}}}}}}}}}
attributes = ['date', 'plant-stand', 'precip', 'temp', 'hail', 'crop-hist', 'area-damaged', 'severity', 'seed-tmt', 'germination', 'plant-growth', 'leaves', 'leafspots-halo', 'leafspots-marg', 'leafspot-size', 'leaf-shread', 'leaf-malf', 'leaf-mild', 'stem', 'lodging', 'stem-cankers', 'canker-lesion', 'fruiting-bodies', 'external-decay', 'mycelium', 'int-discolor', 'sclerotia', 'fruit-pods', 'fruit-spots', 'seed', 'mold-growth', 'seed-discolor', 'seed-size', 'shriveling', 'roots', 'class']
count = 0
for entry in data:
	count += 1
	tempDict = tree.copy()
	result = ""
	while(isinstance(tempDict, dict)):
		root = Node.Node(tempDict.keys()[0], tempDict[tempDict.keys()[0]])
		tempDict = tempDict[tempDict.keys()[0]]
		index = attributes.index(root.value)
		value = entry[index]
		if(value in tempDict.keys()):
			child = Node.Node(value, tempDict[value])
			result = tempDict[value]
			tempDict = tempDict[value]
		else:
			print "can't process input %s" % count
			result = "?"
			break
	print ("entry%s = %s" % (count, result))
