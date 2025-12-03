# Function to download and save an image from a URL
function Save-ImageFromUrl {
    param(
        [Parameter(Mandatory=$true)]
        [string]$ImageUrl,
        [Parameter(Mandatory=$true)]
        [string]$OutputPath
    )
    
    try {
        # Ensure the output directory exists
        $outputDir = [System.IO.Path]::GetDirectoryName($OutputPath)
        if (-not (Test-Path -Path $outputDir)) {
            New-Item -ItemType Directory -Path $outputDir -Force | Out-Null
        }
        
        # Download and save the image
        $response = Invoke-WebRequest -Uri $ImageUrl -UseBasicParsing -ErrorAction Stop
        [System.IO.File]::WriteAllBytes($OutputPath, $response.Content)
        
        Write-Host "Image successfully saved to: $OutputPath" -ForegroundColor Green
        return $true
    } catch {
        Write-Error "Error downloading image from '$ImageUrl': $_"
        return $false
    }
}

# Example usage:
# Save-ImageFromUrl -ImageUrl "https://example.com/image.jpg" -OutputPath "c:\path\to\save\image.jpg"
