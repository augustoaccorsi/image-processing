import logo from './logo.svg';
import './App.css';
import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Input from '@material-ui/core/Input';
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import FormControl from '@material-ui/core/FormControl';
import Container from '@material-ui/core/Container';
import Icon from '@material-ui/core/Icon';
import IconButton from '@material-ui/core/IconButton';
import ButtonGroup from '@material-ui/core/ButtonGroup';
import Dialog from '@material-ui/core/Dialog';
import DialogContentText from '@material-ui/core/DialogContentText';
import useMediaQuery from '@material-ui/core/useMediaQuery';
import { useTheme } from '@material-ui/core/styles';
import { withStyles } from '@material-ui/core/styles';
import MuiDialogTitle from '@material-ui/core/DialogTitle';
import MuiDialogContent from '@material-ui/core/DialogContent';
import MuiDialogActions from '@material-ui/core/DialogActions';
import CloseIcon from '@material-ui/icons/Close';
import Typography from '@material-ui/core/Typography';

//import PhotoCamera from '@material-ui/icons/PhotoCamera';


const useStyles = makeStyles((theme) => ({
  root: {
    '& > *': {
      margin: theme.spacing(1),
    },
  },
  input: {
    display: 'none',
  },
}))

const useStylesText = makeStyles((theme) => ({
  root: {
    ...theme.typography.button,
    backgroundColor: "#282c34",
    padding: theme.spacing(1),
  },
}))

const styles = (theme) => ({
  root: {
    margin: 0,
    padding: theme.spacing(2),
  },
  closeButton: {
    position: 'absolute',
    right: theme.spacing(1),
    top: theme.spacing(1),
    color: theme.palette.grey[500],
  },
});


const DialogTitle = withStyles(styles)((props) => {
  const { children, classes, onClose, ...other } = props;
  return (
    <MuiDialogTitle disableTypography className={classes.root} {...other}>
      <Typography variant="h6">{children}</Typography>
      {onClose ? (
        <IconButton aria-label="close" className={classes.closeButton} onClick={onClose}>
            <CloseIcon />
        </IconButton>
      ) : null}
    </MuiDialogTitle>
  );
});

const DialogContent = withStyles((theme) => ({
  root: {
    padding: theme.spacing(2),
  },
}))(MuiDialogContent);

const DialogActions = withStyles((theme) => ({
  root: {
    margin: 0,
    padding: theme.spacing(1),
  },
}))(MuiDialogActions);

export default function App() {

  const text = useStylesText();
  const [open, setOpen] = React.useState(false);
  const [openEdge, setOpenEdge] = React.useState(false);
  const [openMand, setOpenMand] = React.useState(false);
  const [openUp, setOpenUp] = React.useState(false);
  const [openAll, setOpenAll] = React.useState(false);
  const [openSingle, setOpenSingle] = React.useState(false);
  const theme = useTheme();
  const fullScreen = useMediaQuery(theme.breakpoints.down('sm'));
  const classes = useStyles();

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  const handleClickOpenEdge = () => {
    setOpenEdge(true);
  };

  const handleCloseEdge = () => {
    setOpenEdge(false);
  };

  const handleClickOpenMand = () => {
    setOpenMand(true);
  };

  const handleCloseMand = () => {
    setOpenMand(false);
  };

  const handleClickOpenUp = () => {
    setOpenUp(true);
  };

  const handleCloseUp = () => {
    setOpenUp(false);
  };

  const handleClickOpenAll = () => {
    setOpenAll(true);
  };

  const handleCloseAll = () => {
    setOpenAll(false);
  };

  const handleClickOpenSingle = () => {
    setOpenSingle(true);
  };

  const handleCloseSingle = () => {
    setOpenSingle(false);
  };


  return (
    <div className="App">
   <header className="App-header">
      <div className="App-title">José Augusto Accorsi - Ciência da Computação Unisinos</div>
      <Container maxWidth="lg">
         <Container maxWidth="sm">
            Image Processing
            <ButtonGroup size="large" variant="contained" color="primary" aria-label="contained primary button group">
               <Button onClick={handleClickOpen}>Tranform Image</Button>
               <Dialog onClose={handleClose} aria-labelledby="customized-dialog-title" open={open}>
                  <DialogTitle id="customized-dialog-title" onClose={handleClose}>
                     Transform Image
                  </DialogTitle>
                  <DialogContent>
                     <TextField label="Rotate" color="primary" />
                     <TextField label="Thumb" color="primary" />
                     <TextField label="Compress" color="primary" />
                     <TextField label="Blur" color="primary" />
                  </DialogContent>
                  <DialogActions>
                     <Button autoFocus onClick={handleClose} color="primary">
                     Upload Image
                     </Button>
                     <Button autoFocus onClick={handleClose} color="primary">
                     Execute
                     </Button>
                  </DialogActions>
               </Dialog>
               <Button onClick={handleClickOpenEdge}>Edge</Button>
               <Dialog onClose={handleCloseEdge} aria-labelledby="customized-dialog-title" open={openEdge}>
                  <DialogTitle id="customized-dialog-title" onClose={handleCloseEdge}>
                     Edge Image
                  </DialogTitle>
                  <DialogActions>
                     <Button autoFocus onClick={handleCloseEdge} color="primary">
                     Upload Image
                     </Button>
                     <Button autoFocus onClick={handleCloseEdge} color="primary">
                     Execute
                     </Button>
                  </DialogActions>
               </Dialog>
               <Button onClick={handleClickOpenMand}>Mandelbrot Set</Button>
               <Dialog onClose={handleCloseMand} aria-labelledby="customized-dialog-title" open={openMand}>
                  <DialogTitle id="customized-dialog-title" onClose={handleCloseMand}>
                     Mandelbrot Set
                  </DialogTitle>
                  <DialogContent>
                     <TextField label="Width" color="primary" />
                     <TextField label="Height" color="primary" />
                     <TextField label="Maximun Iterations" color="primary" />
                  </DialogContent>
                  <DialogActions>
                     <Button autoFocus onClick={handleCloseMand} color="primary">
                     Execute
                     </Button>
                  </DialogActions>
               </Dialog>
            </ButtonGroup>
         </Container>
         <p></p>
         <p></p>
         <p></p>
         <p></p>
         <Container maxWidth="sm">
            Database
            <ButtonGroup size="large" variant="contained" color="secondary" aria-label="contained primary button group">
               <Button onClick={handleClickOpenUp}>Upload Image</Button>
               <Dialog onClose={handleCloseUp} aria-labelledby="customized-dialog-title" open={openUp}>
                  <DialogTitle id="customized-dialog-title" onClose={handleCloseUp}>
                     Upload Image
                  </DialogTitle>
                  <DialogContent>
                     <input
                        accept="image/*"
                        className={classes.input}
                        id="contained-button-file"
                        multiple
                        type="file"
                        />
                     <label htmlFor="contained-button-file">
                     <Button variant="contained" color="primary" component="span">
                     Upload
                     </Button>
                     </label>
                  </DialogContent>
                  <DialogActions>
                     <Button autoFocus onClick={handleCloseUp} color="primary">
                     Save
                     </Button>
                  </DialogActions>
               </Dialog>
               <Button onClick={handleClickOpenAll}>Get Images</Button>
               <Dialog onClose={handleCloseAll} aria-labelledby="customized-dialog-title" open={openAll}>
                  <DialogTitle id="customized-dialog-title" onClose={handleCloseAll}>
                     Databe Images
                  </DialogTitle>
                  <DialogContent>
                     Image 1: 3f68a3ab2fa14d0baf58d7d1e66c03ea 
                     <p></p>
                     Image 2: 3f68a3ab2fa14d0baf58d7d1e66c03ea 
                     <p></p>
                     Image 3: 3f68a3ab2fa14d0baf58d7d1e66c03ea
                  </DialogContent>
                  <DialogActions>
                     <Button autoFocus onClick={handleCloseAll} color="primary">
                     Open
                     </Button>
                  </DialogActions>
               </Dialog>
               <Button onClick={handleClickOpenSingle}>Get Single</Button>
               <Dialog onClose={handleCloseSingle} aria-labelledby="customized-dialog-title" open={openSingle}>
                  <DialogTitle id="customized-dialog-title" onClose={handleCloseSingle}>
                     Databe Images
                  </DialogTitle>
                  <DialogContent>
                     <TextField label="Image ID" color="primary" />
                  </DialogContent>
                  <DialogActions>
                     <Button autoFocus onClick={handleCloseSingle} color="primary">
                     Open
                     </Button>
                     <Button autoFocus onClick={handleCloseSingle} color="primary">
                     Download
                     </Button>
                  </DialogActions>
               </Dialog>
            </ButtonGroup>
         </Container>
      </Container>
      <a
         className="App-link"
         href="https://reactjs.org"
         target="_blank"
         rel="noopener noreferrer"
         >
      Microservice Repository
      </a>
   </header>
</div>
  );
}

