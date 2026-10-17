#
# Copyright (C) 2026 The Android Open Source Project
# Copyright (C) 2026 SebaUbuntu's TWRP device tree generator
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit some common Omni stuff.
$(call inherit-product, vendor/omni/config/common.mk)

# Inherit from a24 device
$(call inherit-product, device/samsung/a24/device.mk)

PRODUCT_DEVICE := a24
PRODUCT_NAME := omni_a24
PRODUCT_BRAND := samsung
PRODUCT_MODEL := SM-A245M
PRODUCT_MANUFACTURER := samsung

PRODUCT_GMS_CLIENTID_BASE := android-samsung

PRODUCT_BUILD_PROP_OVERRIDES += \
    PRIVATE_BUILD_DESC="a24ub-user 16 BP2A.250605.031.A3 A245MUBSCEZB5 release-keys"

BUILD_FINGERPRINT := samsung/a24ub/a24:16/BP2A.250605.031.A3/A245MUBSCEZB5:user/release-keys
