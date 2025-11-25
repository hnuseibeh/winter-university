// Link validation and checking
document.addEventListener('DOMContentLoaded', () => {
    // Check if links are accessible (for production)
    const checkLinks = () => {
        const links = document.querySelectorAll('a[href]');
        links.forEach(link => {
            const href = link.getAttribute('href');
            
            // Skip external links and anchors
            if (href.startsWith('http') || href.startsWith('#') || href.startsWith('mailto:')) {
                return;
            }
            
            // Add click handler to verify link works
            link.addEventListener('click', (e) => {
                // For relative paths, let the browser handle it
                // If it's a broken link, the browser will show 404
                // We can add visual feedback here if needed
            });
        });
    };
    
    // Check if we're in production (winter.digital-economy.org)
    const isProduction = window.location.hostname === 'winter.digital-economy.org' || 
                        window.location.hostname.includes('digital-economy.org');
    
    if (isProduction) {
        // In production, we might need to adjust paths
        // This could be handled server-side or via configuration
        console.log('Production environment detected');
    }
    
    checkLinks();
});

// Helper function to update student repo link when available
function updateStudentRepoLink(url) {
    const linkElement = document.getElementById('student-repo-link');
    if (linkElement && url) {
        linkElement.innerHTML = `<a href="${url}" target="_blank" rel="noopener noreferrer">${url}</a>`;
        linkElement.classList.add('active-link');
    }
}

