import * as React from 'react';
import { Link } from 'react-router-dom'
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import CssBaseline from '@mui/material/CssBaseline';
import Divider from '@mui/material/Divider';
import Drawer from '@mui/material/Drawer';
import IconButton from '@mui/material/IconButton';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemText from '@mui/material/ListItemText';
import MenuIcon from '@mui/icons-material/Menu';
import Toolbar from '@mui/material/Toolbar';
import Button from '@mui/material/Button';
import { IoPaw } from "react-icons/io5";
import { FaChevronRight } from "react-icons/fa";

const drawerWidth = 240;
// const navItems = [
//     {name: 'Volunteer', to: "/events"},
//     {name: 'View Pets', to: "/pets"}, 
//     {name: 'Login', to: "/login"}];

const Header = (props) => {
    const { window } = props;
    const [mobileOpen, setMobileOpen] = React.useState(false);

    const handleDrawerToggle = () => {
        setMobileOpen((prevState) => !prevState);
    };

    const drawer = (
        <Box id="drawer" onClick={handleDrawerToggle} sx={{ textAlign: 'left' }}>
        <h2><FaChevronRight /></h2>
        <Divider />
        <List>
            <ListItem disablePadding>
                <ListItemButton sx={{ textAlign: 'left' }}>
                    <ListItemText primary="Volunteer" />
                </ListItemButton>
            </ListItem>
        </List>
        </Box>
    );

    const container = window !== undefined ? () => window().document.body : undefined;

    return (
        <Box id="box" sx={{ display: 'flex' }}>
        <CssBaseline />
        <AppBar  id="header" component="nav">
            <Toolbar>
            <h1>
                <Link to="/">
                    <IoPaw /> Paw-sibilities Rescue
                </Link>
            </h1>
            <IconButton
                color="inherit"
                aria-label="open drawer"
                edge="end"
                onClick={handleDrawerToggle}
                sx={{ mr: 2, display: { sm: 'none' } }}
            >
                <MenuIcon />
            </IconButton>
            <Box sx={{ display: { xs: 'none', sm: 'block' } }}>
                <Link to="/events">
                    <Button sx={{ color: '#fff' }}>
                        Volunteer
                    </Button>
                </Link>
                <Link to="/pets">
                    <Button sx={{ color: '#fff' }}>
                        View Pets
                    </Button>
                </Link>
                <Link to="/login">
                    <Button sx={{ color: '#fff' }}>
                        Login
                    </Button>
                </Link>
            </Box>
            </Toolbar>
        </AppBar>
        <nav>
            <Drawer
            anchor="right"
            container={container}
            variant="temporary"
            open={mobileOpen}
            onClose={handleDrawerToggle}
            ModalProps={{
                keepMounted: true, // Better open performance on mobile.
            }}
            sx={{
                display: { xs: 'block', sm: 'none' },
                '& .MuiDrawer-paper': { boxSizing: 'border-box', width: drawerWidth },
            }}
            >
            {drawer}
            </Drawer>
        </nav>
        <Box component="main" sx={{ p: 3 }}>
            <Toolbar />
        </Box>
        </Box>
    )
}

export default Header