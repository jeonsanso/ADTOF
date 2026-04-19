import os

# tf_keras (Keras 2) must be active before TensorFlow is imported.
# The saved model weights use the legacy TF checkpoint format which
# Keras 3 no longer supports.
os.environ.setdefault("TF_USE_LEGACY_KERAS", "1")
