import numpy as np
import rasterio
from rasterio.transform import from_origin

#---------------------------------------------------------------------------------------------------------
#2009
#---------------------------------------------------------------------------------------------------------
#50 trees
#load result
a = np.load('/Volumes/ga87rif/Study Project/Result/New/result09_50trees.npy')
a = a.astype(np.uint8)

#reshape into 2D
b = np.reshape(a, (-1,3057))
c = np.flipud(b) #flip vertically
#because rasterio is lame it writes from bottom to top

#transform = from_origin(110....<--dari origin, -7....<--bukan dari origin, 0.000271658, -0.000271658)
transform = from_origin(110.0363020639564269, -7.8701315292535803, 0.000271658, -0.000271658)

new_dataset = rasterio.open('/Volumes/ga87rif/Study Project/Result/New/result09_50trees.tif', 'w', driver='GTiff',
                            height = b.shape[0], width = c.shape[1],
                            count=1, dtype=c.dtype,
                            crs='+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs',
                            transform=transform)

new_dataset.write(c, 1)
new_dataset.close()

#---------------------------------------------------------------------------------------------------------
#100 trees
#load result
a = np.load('/Volumes/ga87rif/Study Project/Result/New/result09_100trees.npy')
a = a.astype(np.uint8)

#reshape into 2D
b = np.reshape(a, (-1,3057))
c = np.flipud(b) #flip vertically
#because rasterio is lame it writes from bottom to top

#transform = from_origin(110....<--dari origin, -7....<--bukan dari origin, 0.000271658, -0.000271658)
transform = from_origin(110.0363020639564269, -7.8701315292535803, 0.000271658, -0.000271658)

new_dataset = rasterio.open('/Volumes/ga87rif/Study Project/Result/New/result09_100trees.tif', 'w', driver='GTiff',
                            height = b.shape[0], width = c.shape[1],
                            count=1, dtype=c.dtype,
                            crs='+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs',
                            transform=transform)

new_dataset.write(c, 1)
new_dataset.close()

#---------------------------------------------------------------------------------------------------------
#200 trees
#load result
a = np.load('/Volumes/ga87rif/Study Project/Result/New/result09_200trees.npy')
a = a.astype(np.uint8)

#reshape into 2D
b = np.reshape(a, (-1,3057))
c = np.flipud(b) #flip vertically
#because rasterio is lame it writes from bottom to top

#transform = from_origin(110....<--dari origin, -7....<--bukan dari origin, 0.000271658, -0.000271658)
transform = from_origin(110.0363020639564269, -7.8701315292535803, 0.000271658, -0.000271658)

new_dataset = rasterio.open('/Volumes/ga87rif/Study Project/Result/New/result09_200trees.tif', 'w', driver='GTiff',
                            height = b.shape[0], width = c.shape[1],
                            count=1, dtype=c.dtype,
                            crs='+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs',
                            transform=transform)

new_dataset.write(c, 1)
new_dataset.close()

#---------------------------------------------------------------------------------------------------------
#300 trees
#load result
a = np.load('/Volumes/ga87rif/Study Project/Result/New/result09_300trees.npy')
a = a.astype(np.uint8)

#reshape into 2D
b = np.reshape(a, (-1,3057))
c = np.flipud(b) #flip vertically
#because rasterio is lame it writes from bottom to top

#transform = from_origin(110....<--dari origin, -7....<--bukan dari origin, 0.000271658, -0.000271658)
transform = from_origin(110.0363020639564269, -7.8701315292535803, 0.000271658, -0.000271658)

new_dataset = rasterio.open('/Volumes/ga87rif/Study Project/Result/New/result09_300trees.tif', 'w', driver='GTiff',
                            height = b.shape[0], width = c.shape[1],
                            count=1, dtype=c.dtype,
                            crs='+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs',
                            transform=transform)

new_dataset.write(c, 1)
new_dataset.close()

#---------------------------------------------------------------------------------------------------------
#400 trees
#load result
a = np.load('/Volumes/ga87rif/Study Project/Result/New/result09_400trees.npy')
a = a.astype(np.uint8)

#reshape into 2D
b = np.reshape(a, (-1,3057))
c = np.flipud(b) #flip vertically
#because rasterio is lame it writes from bottom to top

#transform = from_origin(110....<--dari origin, -7....<--bukan dari origin, 0.000271658, -0.000271658)
transform = from_origin(110.0363020639564269, -7.8701315292535803, 0.000271658, -0.000271658)

new_dataset = rasterio.open('/Volumes/ga87rif/Study Project/Result/New/result09_400trees.tif', 'w', driver='GTiff',
                            height = b.shape[0], width = c.shape[1],
                            count=1, dtype=c.dtype,
                            crs='+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs',
                            transform=transform)

new_dataset.write(c, 1)
new_dataset.close()

#---------------------------------------------------------------------------------------------------------
#500 trees
#load result
a = np.load('/Volumes/ga87rif/Study Project/Result/New/result09_500trees.npy')
a = a.astype(np.uint8)

#reshape into 2D
b = np.reshape(a, (-1,3057))
c = np.flipud(b) #flip vertically
#because rasterio is lame it writes from bottom to top

#transform = from_origin(110....<--dari origin, -7....<--bukan dari origin, 0.000271658, -0.000271658)
transform = from_origin(110.0363020639564269, -7.8701315292535803, 0.000271658, -0.000271658)

new_dataset = rasterio.open('/Volumes/ga87rif/Study Project/Result/New/result09_500trees.tif', 'w', driver='GTiff',
                            height = b.shape[0], width = c.shape[1],
                            count=1, dtype=c.dtype,
                            crs='+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs',
                            transform=transform)

new_dataset.write(c, 1)
new_dataset.close()

#---------------------------------------------------------------------------------------------------------
#750 trees
#load result
a = np.load('/Volumes/ga87rif/Study Project/Result/New/result09_750trees.npy')
a = a.astype(np.uint8)

#reshape into 2D
b = np.reshape(a, (-1,3057))
c = np.flipud(b) #flip vertically
#because rasterio is lame it writes from bottom to top

#transform = from_origin(110....<--dari origin, -7....<--bukan dari origin, 0.000271658, -0.000271658)
transform = from_origin(110.0363020639564269, -7.8701315292535803, 0.000271658, -0.000271658)

new_dataset = rasterio.open('/Volumes/ga87rif/Study Project/Result/New/result09_750trees.tif', 'w', driver='GTiff',
                            height = b.shape[0], width = c.shape[1],
                            count=1, dtype=c.dtype,
                            crs='+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs',
                            transform=transform)

new_dataset.write(c, 1)
new_dataset.close()

#---------------------------------------------------------------------------------------------------------
#1000 trees
#load result
a = np.load('/Volumes/ga87rif/Study Project/Result/New/result09_1000trees.npy')
a = a.astype(np.uint8)

#reshape into 2D
b = np.reshape(a, (-1,3057))
c = np.flipud(b) #flip vertically
#because rasterio is lame it writes from bottom to top

#transform = from_origin(110....<--dari origin, -7....<--bukan dari origin, 0.000271658, -0.000271658)
transform = from_origin(110.0363020639564269, -7.8701315292535803, 0.000271658, -0.000271658)

new_dataset = rasterio.open('/Volumes/ga87rif/Study Project/Result/New/result09_1000trees.tif', 'w', driver='GTiff',
                            height = b.shape[0], width = c.shape[1],
                            count=1, dtype=c.dtype,
                            crs='+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs',
                            transform=transform)

new_dataset.write(c, 1)
new_dataset.close()

#---------------------------------------------------------------------------------------------------------
#2011
#---------------------------------------------------------------------------------------------------------
#50 trees
#load result
a = np.load('/Volumes/ga87rif/Study Project/Result/New/result11_50trees.npy')
a = a.astype(np.uint8)

#reshape into 2D
b = np.reshape(a, (-1,3057))
c = np.flipud(b) #flip vertically
#because rasterio is lame it writes from bottom to top

#transform = from_origin(110....<--dari origin, -7....<--bukan dari origin, 0.000271658, -0.000271658)
transform = from_origin(110.0363020639564269, -7.8701315292535803, 0.000271658, -0.000271658)

new_dataset = rasterio.open('/Volumes/ga87rif/Study Project/Result/New/result11_50trees.tif', 'w', driver='GTiff',
                            height = b.shape[0], width = c.shape[1],
                            count=1, dtype=c.dtype,
                            crs='+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs',
                            transform=transform)

new_dataset.write(c, 1)
new_dataset.close()

#---------------------------------------------------------------------------------------------------------
#100 trees
#load result
a = np.load('/Volumes/ga87rif/Study Project/Result/New/result11_100trees.npy')
a = a.astype(np.uint8)

#reshape into 2D
b = np.reshape(a, (-1,3057))
c = np.flipud(b) #flip vertically
#because rasterio is lame it writes from bottom to top

#transform = from_origin(110....<--dari origin, -7....<--bukan dari origin, 0.000271658, -0.000271658)
transform = from_origin(110.0363020639564269, -7.8701315292535803, 0.000271658, -0.000271658)

new_dataset = rasterio.open('/Volumes/ga87rif/Study Project/Result/New/result11_100trees.tif', 'w', driver='GTiff',
                            height = b.shape[0], width = c.shape[1],
                            count=1, dtype=c.dtype,
                            crs='+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs',
                            transform=transform)

new_dataset.write(c, 1)
new_dataset.close()

#---------------------------------------------------------------------------------------------------------
#200 trees
#load result
a = np.load('/Volumes/ga87rif/Study Project/Result/New/result11_200trees.npy')
a = a.astype(np.uint8)

#reshape into 2D
b = np.reshape(a, (-1,3057))
c = np.flipud(b) #flip vertically
#because rasterio is lame it writes from bottom to top

#transform = from_origin(110....<--dari origin, -7....<--bukan dari origin, 0.000271658, -0.000271658)
transform = from_origin(110.0363020639564269, -7.8701315292535803, 0.000271658, -0.000271658)

new_dataset = rasterio.open('/Volumes/ga87rif/Study Project/Result/New/result11_200trees.tif', 'w', driver='GTiff',
                            height = b.shape[0], width = c.shape[1],
                            count=1, dtype=c.dtype,
                            crs='+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs',
                            transform=transform)

new_dataset.write(c, 1)
new_dataset.close()

#---------------------------------------------------------------------------------------------------------
#300 trees
#load result
a = np.load('/Volumes/ga87rif/Study Project/Result/New/result11_300trees.npy')
a = a.astype(np.uint8)

#reshape into 2D
b = np.reshape(a, (-1,3057))
c = np.flipud(b) #flip vertically
#because rasterio is lame it writes from bottom to top

#transform = from_origin(110....<--dari origin, -7....<--bukan dari origin, 0.000271658, -0.000271658)
transform = from_origin(110.0363020639564269, -7.8701315292535803, 0.000271658, -0.000271658)

new_dataset = rasterio.open('/Volumes/ga87rif/Study Project/Result/New/result11_300trees.tif', 'w', driver='GTiff',
                            height = b.shape[0], width = c.shape[1],
                            count=1, dtype=c.dtype,
                            crs='+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs',
                            transform=transform)

new_dataset.write(c, 1)
new_dataset.close()

#---------------------------------------------------------------------------------------------------------
#400 trees
#load result
a = np.load('/Volumes/ga87rif/Study Project/Result/New/result11_400trees.npy')
a = a.astype(np.uint8)

#reshape into 2D
b = np.reshape(a, (-1,3057))
c = np.flipud(b) #flip vertically
#because rasterio is lame it writes from bottom to top

#transform = from_origin(110....<--dari origin, -7....<--bukan dari origin, 0.000271658, -0.000271658)
transform = from_origin(110.0363020639564269, -7.8701315292535803, 0.000271658, -0.000271658)

new_dataset = rasterio.open('/Volumes/ga87rif/Study Project/Result/New/result11_400trees.tif', 'w', driver='GTiff',
                            height = b.shape[0], width = c.shape[1],
                            count=1, dtype=c.dtype,
                            crs='+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs',
                            transform=transform)

new_dataset.write(c, 1)
new_dataset.close()

#---------------------------------------------------------------------------------------------------------
#500 trees
#load result
a = np.load('/Volumes/ga87rif/Study Project/Result/New/result11_500trees.npy')
a = a.astype(np.uint8)

#reshape into 2D
b = np.reshape(a, (-1,3057))
c = np.flipud(b) #flip vertically
#because rasterio is lame it writes from bottom to top

#transform = from_origin(110....<--dari origin, -7....<--bukan dari origin, 0.000271658, -0.000271658)
transform = from_origin(110.0363020639564269, -7.8701315292535803, 0.000271658, -0.000271658)

new_dataset = rasterio.open('/Volumes/ga87rif/Study Project/Result/New/result11_500trees.tif', 'w', driver='GTiff',
                            height = b.shape[0], width = c.shape[1],
                            count=1, dtype=c.dtype,
                            crs='+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs',
                            transform=transform)

new_dataset.write(c, 1)
new_dataset.close()

#---------------------------------------------------------------------------------------------------------
#750 trees
#load result
a = np.load('/Volumes/ga87rif/Study Project/Result/New/result11_750trees.npy')
a = a.astype(np.uint8)

#reshape into 2D
b = np.reshape(a, (-1,3057))
c = np.flipud(b) #flip vertically
#because rasterio is lame it writes from bottom to top

#transform = from_origin(110....<--dari origin, -7....<--bukan dari origin, 0.000271658, -0.000271658)
transform = from_origin(110.0363020639564269, -7.8701315292535803, 0.000271658, -0.000271658)

new_dataset = rasterio.open('/Volumes/ga87rif/Study Project/Result/New/result11_750trees.tif', 'w', driver='GTiff',
                            height = b.shape[0], width = c.shape[1],
                            count=1, dtype=c.dtype,
                            crs='+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs',
                            transform=transform)

new_dataset.write(c, 1)
new_dataset.close()

#---------------------------------------------------------------------------------------------------------
#1000 trees
#load result
a = np.load('/Volumes/ga87rif/Study Project/Result/New/result11_1000trees.npy')
a = a.astype(np.uint8)

#reshape into 2D
b = np.reshape(a, (-1,3057))
c = np.flipud(b) #flip vertically
#because rasterio is lame it writes from bottom to top

#transform = from_origin(110....<--dari origin, -7....<--bukan dari origin, 0.000271658, -0.000271658)
transform = from_origin(110.0363020639564269, -7.8701315292535803, 0.000271658, -0.000271658)

new_dataset = rasterio.open('/Volumes/ga87rif/Study Project/Result/New/result11_1000trees.tif', 'w', driver='GTiff',
                            height = b.shape[0], width = c.shape[1],
                            count=1, dtype=c.dtype,
                            crs='+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs',
                            transform=transform)

new_dataset.write(c, 1)
new_dataset.close()

