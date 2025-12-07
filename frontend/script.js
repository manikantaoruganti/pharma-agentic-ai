// Drug Discovery Search Form Handler
document.getElementById('searchForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const moleculeName = document.getElementById('moleculeName').value;
    const diseaseArea = document.getElementById('diseaseArea').value;
    
    console.log('Searching for:', { moleculeName, diseaseArea });
    
    try {
        // Call API endpoint
        const response = await fetch('/api/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ molecule_name: moleculeName, disease_area: diseaseArea })
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        displayResults(data);
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('results').innerHTML = `<p>Error: ${error.message}</p>`;
    }
});

function displayResults(data) {
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = '';
    
    if (!data || data.length === 0) {
        resultsDiv.innerHTML = '<p>No results found</p>';
        return;
    }
    
    const resultsList = document.createElement('ul');
    data.forEach(result => {
        const li = document.createElement('li');
        li.textContent = JSON.stringify(result, null, 2);
        resultsList.appendChild(li);
    });
    
    resultsDiv.appendChild(resultsList);
}

console.log('Script loaded successfully');
