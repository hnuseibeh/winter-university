// Link validation and checking with internal/external fallback
document.addEventListener('DOMContentLoaded', () => {
    // Check if internal links are accessible
    const checkInternalLinks = async () => {
        const internalLinks = [
            { selector: 'a[href="../reference-dashboard/"]', fallback: 'https://github.com/hnuseibeh/winter-university/tree/main/reference-dashboard' },
            { selector: 'a[href="../reference-dashboard/README.md"]', fallback: 'https://github.com/hnuseibeh/winter-university/blob/main/reference-dashboard/README.md' },
            { selector: 'a[href="../reference-examples/"]', fallback: 'https://github.com/hnuseibeh/winter-university/tree/main/reference-examples' },
            { selector: 'a[href="../reference-examples/README.md"]', fallback: 'https://github.com/hnuseibeh/winter-university/blob/main/reference-examples/README.md' }
        ];

        for (const linkInfo of internalLinks) {
            const link = document.querySelector(linkInfo.selector);
            if (!link) continue;

            try {
                // Try to fetch the link to see if it exists
                const response = await fetch(link.getAttribute('href'), { method: 'HEAD' });
                if (!response.ok) {
                    // If internal link doesn't work, update to GitHub fallback
                    link.href = linkInfo.fallback;
                    link.target = '_blank';
                    link.rel = 'noopener noreferrer';
                    link.classList.add('external-link');
                }
            } catch (error) {
                // If fetch fails (CORS, network error, etc.), assume internal link might work
                // But add a click handler to check on actual click
                link.addEventListener('click', (e) => {
                    // Let the browser try the internal link first
                    // If it fails, user will see 404 and can use GitHub link
                });
            }
        }
    };

    // Check if we're in production (winter.digital-economy.org)
    const isProduction = window.location.hostname === 'winter.digital-economy.org' || 
                        window.location.hostname.includes('digital-economy.org');
    
    if (isProduction) {
        // In production, try to verify internal links
        checkInternalLinks();
    } else {
        // In local development, internal links should work
        console.log('Local development - using internal links');
    }
});

// Helper function to update student repo link when available
function updateStudentRepoLink(url) {
    const linkElement = document.getElementById('student-repo-link');
    if (linkElement && url) {
        linkElement.innerHTML = `<a href="${url}" target="_blank" rel="noopener noreferrer">${url}</a>`;
        linkElement.classList.add('active-link');
    }
}

