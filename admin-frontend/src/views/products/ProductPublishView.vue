<template>
  <div class="product-publish-page">
    <el-form :model="productForm"
      @submit.prevent="handleProductPublish()"
    >
      <div class="product-form-section">
        <div class="product-form-section__header">
          基础信息
        </div>

        <div class="product-form-section__content">
          <el-form-item label="商品标题：">
            <el-input
                v-model="productForm.productName"
                maxlength="100"
                placeholder="请输入商品标题"
            ></el-input>
          </el-form-item>

          <el-form-item label="商品类目：">
            <el-select
                v-model="productForm.productCategory"
                placeholder="请选择商品种类"
            >
              <el-option
                  v-for="category in PRODUCT_CATEGORY_OPTIONS"
                  :key="category.value"
                  :label="category.label"
                  :value="category.value"
              ></el-option>
            </el-select>
          </el-form-item>

          <el-form-item label="商品编号：">
            <el-input
                v-model="productForm.productCode"
                maxlength="50"
                placeholder="请输入商品编号"
            ></el-input>
          </el-form-item>
        </div>
      </div>

      <div class="product-form-section">
        <div class="product-form-section__header">
          销售属性
        </div>

        <div class="product-form-section__content">
          <el-form-item label="商品价格：">
            <el-input-number
                v-model="productForm.price"
                :min="0.01"
                :precision="2"
                :step="0.01"
                :controls="false"
            >
              <template #suffix>元</template>
            </el-input-number>
          </el-form-item>

          <el-form-item label="履约时限：">
            <el-input-number
                v-model="productForm.deliveryTimeLimitDays"
                :min="1"
                :step="1"
                step-strictly
                :controls="false"
            >
              <template #suffix>天</template>
            </el-input-number>
          </el-form-item>
        </div>
      </div>

      <div class="product-form-section">
        <div class="product-form-section__header">
          图文描述
        </div>

        <div class="product-form-section__content">
          <div class="product-image-field">
            <div class="product-image-field__label">
              主图：订购页面展示图片
            </div>

            <el-upload
                v-model:file-list="productFile.mainImageFiles"
                :auto-upload="false"
                :class="{
                  'product-image-upload--filled':
                    productFile.mainImageFiles.length > 0
                }"
                :multiple="false"
                :on-change="(uploadFile: UploadFile) => {
                  productFile.mainImageFiles = getSelectedImageFiles(uploadFile)
                }"
                accept="image/jpeg,image/png"
                list-type="picture-card"
            >
              <span>选择主图</span>
            </el-upload>
          </div>
        </div>

        <div class="product-image-field">
          <div class="product-image-field__label">
            详情图：商品详情页展示图片，至多可上传5张
          </div>

          <div class="product-detail-image-slots">
            <el-upload
                v-model:file-list="productFile.detailImage1Files"
                :auto-upload="false"
                :class="{
                  'product-image-upload--filled':
                    productFile.detailImage1Files.length > 0
                }"
                              :multiple="false"
                              :on-change="(uploadFile: UploadFile) => {
                  productFile.detailImage1Files = getSelectedImageFiles(uploadFile)
                }"
                accept="image/jpeg,image/png"
                list-type="picture-card"
            >
              <span>详情图</span>
            </el-upload>

            <el-upload
                v-model:file-list="productFile.detailImage2Files"
                :auto-upload="false"
                :class="{
                  'product-image-upload--filled':
                    productFile.detailImage2Files.length > 0
                }"
                :multiple="false"
                :on-change="(uploadFile: UploadFile) => {
                  productFile.detailImage2Files = getSelectedImageFiles(uploadFile)
                }"
                accept="image/jpeg,image/png"
                list-type="picture-card"
            >
              <span>详情图</span>
            </el-upload>

            <el-upload
                v-model:file-list="productFile.detailImage3Files"
                :auto-upload="false"
                :class="{
                  'product-image-upload--filled':
                    productFile.detailImage3Files.length > 0
                }"
                :multiple="false"
                :on-change="(uploadFile: UploadFile) => {
                  productFile.detailImage3Files = getSelectedImageFiles(uploadFile)
                }"
                accept="image/jpeg,image/png"
                list-type="picture-card"
            >
              <span>详情图</span>
            </el-upload>

            <el-upload
                v-model:file-list="productFile.detailImage4Files"
                :auto-upload="false"
                :class="{
                  'product-image-upload--filled':
                    productFile.detailImage4Files.length > 0
                }"
                :multiple="false"
                :on-change="(uploadFile: UploadFile) => {
                  productFile.detailImage4Files = getSelectedImageFiles(uploadFile)
                }"
                accept="image/jpeg,image/png"
                list-type="picture-card"
            >
              <span>详情图</span>
            </el-upload>

            <el-upload
                v-model:file-list="productFile.detailImage5Files"
                :auto-upload="false"
                :class="{
                  'product-image-upload--filled':
                    productFile.detailImage5Files.length > 0
                }"
                :multiple="false"
                :on-change="(uploadFile: UploadFile) => {
                  productFile.detailImage5Files = getSelectedImageFiles(uploadFile)
                }"
                accept="image/jpeg,image/png"
                list-type="picture-card"
            >
              <span>详情图</span>
            </el-upload>
          </div>
        </div>
      </div>

      <div class="product-form-actions">
        <el-button @click="resetProductForm">
          重置
        </el-button>

        <el-button
          type="primary"
          native-type="submit"
        >
          发布商品
        </el-button>
      </div>
    </el-form>
  </div>
</template>

<script setup lang="ts">
import { reactive } from 'vue'
import { ElMessage } from 'element-plus'
import type { UploadFile } from 'element-plus'

import type { ProductPublishForm, ProductPublishFiles } from "../../types/product";

import { PRODUCT_CATEGORY_OPTIONS } from "../../constants/product";
import { publishProduct } from '../../api/product'

const productForm = reactive<ProductPublishForm>({
  productName: '',
  productCategory: undefined,
  productCode: '',
  price: undefined,
  deliveryTimeLimitDays: undefined,
})

const productFile = reactive<ProductPublishFiles>({
  mainImageFiles: [],
  detailImage1Files: [],
  detailImage2Files: [],
  detailImage3Files: [],
  detailImage4Files: [],
  detailImage5Files: [],
})

// 图片格式检查
function getSelectedImageFiles(
    uploadFile: UploadFile,
): UploadFile[] {
  const fileType = uploadFile.raw?.type

  if (fileType !== 'image/jpeg' && fileType !== 'image/png') {
    ElMessage.error('仅支持 JPEG、PNG 格式的图片')
    return []
  }

  return [uploadFile]
}

function resetProductForm(): void {
  productForm.productName = ''
  productForm.productCategory = undefined
  productForm.productCode = ''
  productForm.price = undefined
  productForm.deliveryTimeLimitDays = undefined

  productFile.mainImageFiles = []
  productFile.detailImage1Files = []
  productFile.detailImage2Files = []
  productFile.detailImage3Files = []
  productFile.detailImage4Files = []
  productFile.detailImage5Files = []
}

async function handleProductPublish(): Promise<void> {
  const productName = productForm.productName.trim()
  const productCategory = productForm.productCategory
  const productCode = productForm.productCode.trim()
  const price = productForm.price
  const deliveryTimeLimitDays = productForm.deliveryTimeLimitDays

  if (
    productName === '' ||
    productCategory === undefined ||
    productCode === '' ||
    price === undefined ||
    deliveryTimeLimitDays === undefined
  ) {
    ElMessage.warning('请填写完整商品信息')
    return
  }

  const mainImage = productFile.mainImageFiles[0]?.raw

  if (mainImage === undefined) {
    ElMessage.warning('请选择商品主图')
    return
  }

  try {
    await publishProduct({
      productName,
      productCategory,
      productCode,
      price,
      deliveryTimeLimitMinutes: deliveryTimeLimitDays * 24 * 60,
      mainImage,
      detailImage1: productFile.detailImage1Files[0]?.raw,
      detailImage2: productFile.detailImage2Files[0]?.raw,
      detailImage3: productFile.detailImage3Files[0]?.raw,
      detailImage4: productFile.detailImage4Files[0]?.raw,
      detailImage5: productFile.detailImage5Files[0]?.raw,
    })

    ElMessage.success('商品发布成功')
    resetProductForm()
  } catch {
    ElMessage.error('商品发布失败')
  }
}
</script>

<style scoped>
:deep(
  .el-upload-list--picture-card
  .el-upload-list__item-thumbnail
) {
  object-fit: cover;
}

.product-image-upload--filled :deep(.el-upload--picture-card) {
  display: none;
}

/* 隐藏放大镜图标 */
:deep(
  .el-upload-list--picture-card
  .el-upload-list__item-actions:hover
  .el-upload-list__item-preview
) {
  display: none;
}
</style>
