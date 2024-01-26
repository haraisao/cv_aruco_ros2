from setuptools import setup
import os
from glob import glob

package_name = 'cv_aruco'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Isao Hara',
    maintainer_email='haraisao@gmail.com',
    description='Aruco Maker detection',
    license='MIT License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'aruco_marker_node = cv_aruco.aruco_marker_node:main'
        ],
    },
)
