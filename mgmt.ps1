# Define the root project directory
$rootDir = "factory_management"

# Define the subdirectories to create
$subDirs = @(
    "app",
    "app/blueprints",
    "app/services"
)

# Define the files to create with their paths
$files = @(
    "app/__init__.py",
    "app/config.py",
    "app/extensions.py",
    "app/models.py",
    "app/blueprints/__init__.py",
    "app/blueprints/employees.py",
    "app/blueprints/products.py",
    "app/blueprints/orders.py",
    "app/blueprints/customers.py",
    "app/blueprints/production.py",
    "app/services/__init__.py",
    "app/services/employee_service.py",
    "app/services/product_service.py",
    "app/services/order_service.py",
    "app/services/customer_service.py",
    "app/services/production_service.py",
    "requirements.txt",
    "run.py"
)

# Create the root directory if it does not exist
if (-not (Test-Path -Path $rootDir)) {
    New-Item -ItemType Directory -Path $rootDir -Force
}

# Create the subdirectories if they do not exist
foreach ($subDir in $subDirs) {
    $fullPath = Join-Path -Path $rootDir -ChildPath $subDir
    if (-not (Test-Path -Path $fullPath)) {
        New-Item -ItemType Directory -Path $fullPath -Force
    }
}

# Create the files if they do not exist
foreach ($file in $files) {
    $fullPath = Join-Path -Path $rootDir -ChildPath $file
    if (-not (Test-Path -Path $fullPath)) {
        New-Item -ItemType File -Path $fullPath -Force
    }
}

Write-Output "Project directory structure and files created successfully!"

