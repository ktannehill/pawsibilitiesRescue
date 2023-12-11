import { useState, forwardRef } from "react";
import Snackbar from "@mui/material/Snackbar";
import MuiAlert from "@mui/material/Alert";
import { useDispatch, useSelector } from "react-redux";
import { clearErrors } from '../features/user/userSlice'

const Alert = forwardRef((props, ref) => (
  <MuiAlert elevation={6} ref={ref} variant="filled" {...props} />
));

const AlertBar = () => {
  const userErrors = useSelector(state => state.user.errors)
  // const eventErrors = useSelector(state => state.event.errors)
  // const petErrors = useSelector(state => state.pet.errors)
  const dispatch = useDispatch()
  const [open, setOpen] = useState(true);

  const errors = [...userErrors]

  const handleClose = (event, reason) => {
    if (reason === "clickaway") {
      return;
    }
    setOpen(false);
    if (errors.length) {
      dispatch(clearErrors())
    }
  };

  return (
    <Snackbar open={open} autoHideDuration={5000} onClose={handleClose}>
      <Alert onClose={handleClose} severity="error" sx={{ width: "100%" }}>
        {userErrors[0]}
      </Alert>
    </Snackbar>
  );
};

export default AlertBar;