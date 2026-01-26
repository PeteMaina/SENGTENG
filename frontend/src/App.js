import React from 'react';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import { Container, Typography, Button, Box, AppBar, Toolbar } from '@mui/material';

// Senteng theme
const theme = createTheme({
    palette: {
        primary: {
            main: '#006233',
            light: '#04F404',
        },
        secondary: {
            main: '#ef1821',
        },
    },
    typography: {
        fontFamily: '"Inter", sans-serif',
        h1: {
            fontFamily: '"Abril Fatface", serif',
        },
        h2: {
            fontFamily: '"Abril Fatface", serif',
        },
    },
});

function App() {
    return (
        <ThemeProvider theme={theme}>
            <CssBaseline />

            {/* Navbar */}
            <AppBar position="sticky" color="default" elevation={2}>
                <Toolbar>
                    <Typography variant="h6" sx={{ fontFamily: '"Abril Fatface", serif', color: 'primary.light', flexGrow: 1 }}>
                        SENTENG FASHIONS
                    </Typography>
                    <Button color="primary">Home</Button>
                    <Button color="primary">Shop</Button>
                    <Button color="primary">Quote</Button>
                </Toolbar>
            </AppBar>

            {/* Hero Section */}
            <Box
                sx={{
                    background: 'linear-gradient(to right, #006233, #04F404, #006233)',
                    color: 'white',
                    py: 10,
                    textAlign: 'center',
                }}
            >
                <Container maxWidth="lg">
                    <Typography variant="h2" gutterBottom>
                        Kenya's #1 Choice for Workwear, Uniforms & Branding
                    </Typography>
                    <Typography variant="h5" sx={{ mb: 4 }}>
                        Unmatched quality. Affordable prices. Unlimited customization.
                    </Typography>
                    <Button variant="contained" size="large" sx={{ bgcolor: 'white', color: 'primary.main', mr: 2 }}>
                        Shop Now
                    </Button>
                    <Button variant="outlined" size="large" sx={{ borderColor: 'white', color: 'white' }}>
                        Request Quote
                    </Button>
                </Container>
            </Box>

            {/* About Section */}
            <Container maxWidth="lg" sx={{ py: 8 }}>
                <Typography variant="h3" align="center" gutterBottom color="secondary">
                    Who We Are
                </Typography>
                <Typography paragraph>
                    Senteng Fashions was recently established in Nairobi, Kenya, with a mission to provide high-quality uniforms and workwear solutions to businesses across the country.
                </Typography>
                <Typography paragraph>
                    <strong>We specialize in:</strong> Industrial Wear, Hospitality Wear, Health Care Wear, Corporate Wear, Security Uniforms, Safety Equipment (PPE), Sports Wear, and School Uniforms.
                </Typography>
            </Container>

            {/* Footer */}
            <Box component="footer" sx={{ bgcolor: 'black', color: 'white', py: 4, textAlign: 'center' }}>
                <Typography variant="h6" sx={{ fontFamily: '"Abril Fatface", serif', color: 'primary.light', mb: 2 }}>
                    SENTENG FASHIONS
                </Typography>
                <Typography variant="body2">
                    📍 Mfangano Street, Terry House, 2nd Floor, Nairobi
                </Typography>
                <Typography variant="body2">
                    📞 0725748082, 0733559349
                </Typography>
                <Typography variant="body2">
                    📧 sentengbrands89@gmail.com
                </Typography>
                <Typography variant="body2" sx={{ mt: 2 }}>
                    © 2026 Senteng Fashions. All Rights Reserved.
                </Typography>
            </Box>
        </ThemeProvider>
    );
}

export default App;
