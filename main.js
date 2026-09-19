function generateSKU() {
	const category = document.getElementById("category").value;
	const productName = document.getElementById("productName").value.trim();
	const stockQuantity = document.getElementById("stockQuantity").value;
	const result = document.getElementById("skuResult");

	if (!productName || !stockQuantity) {
		result.textContent = "Please enter a product name and stock quantity.";
		return;
	}

	const categoryCode = category.slice(0, 3).toUpperCase();
	const productCode = productName.slice(0, 3).toUpperCase();
	result.innerHTML = `<p>Generated Code:</p><p><b>${categoryCode}-${productCode}-${stockQuantity}</b></p>`;
}
