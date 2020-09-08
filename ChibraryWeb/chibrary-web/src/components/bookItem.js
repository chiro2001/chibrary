import React from 'react'
import { Link } from 'react-router-dom'
import ArrowBackIcon from '@material-ui/icons/ArrowBack';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import IconButton from '@material-ui/core/IconButton';
import Typography from '@material-ui/core/Typography';
import DehazeIcon from '@material-ui/icons/Dehaze';
import Container from '@material-ui/core/Container';
import Paper from "@material-ui/core/Paper"
import Card from "@material-ui/core/Card"
import Grid from "@material-ui/core/Grid"
import Rating from "@material-ui/lab/Rating"
import Button from "@material-ui/core/Button"
import Accordion from '@material-ui/core/Accordion';
import AccordionSummary from '@material-ui/core/AccordionSummary';
import AccordionDetails from '@material-ui/core/AccordionDetails';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import grey from "@material-ui/core/colors/grey"
import red from "@material-ui/core/colors/red"
import LinearProgress from '@material-ui/core/LinearProgress';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import AtmIcon from '@material-ui/icons/Atm';
import GitHubIcon from '@material-ui/icons/GitHub';
import ArrowRightIcon from '@material-ui/icons/ArrowRight';
import ModeCommentIcon from '@material-ui/icons/ModeComment';
import HomeIcon from '@material-ui/icons/Home';
import ThumbUpIcon from '@material-ui/icons/ThumbUp';
import ForumIcon from '@material-ui/icons/Forum';
import AddIcon from '@material-ui/icons/Add';
import CloudUploadIcon from '@material-ui/icons/CloudUpload';

import RefreshIcon from '@material-ui/icons/Refresh';
import PlaylistAddIcon from '@material-ui/icons/PlaylistAdd';
import Drawer from '@material-ui/core/Drawer';
import useScrollTrigger from '@material-ui/core/useScrollTrigger';
import MuiAlert from '@material-ui/lab/Alert';
import Checkbox from '@material-ui/core/Checkbox';
import Fab from '@material-ui/core/Fab';
import KeyboardArrowUpIcon from '@material-ui/icons/KeyboardArrowUp';
import Zoom from '@material-ui/core/Zoom';
import { fade, makeStyles } from '@material-ui/core/styles';
import InputBase from '@material-ui/core/InputBase';
import Badge from '@material-ui/core/Badge';
import MenuItem from '@material-ui/core/MenuItem';
import Menu from '@material-ui/core/Menu';
import MenuIcon from '@material-ui/icons/Menu';
import SearchIcon from '@material-ui/icons/Search';
import AccountCircle from '@material-ui/icons/AccountCircle';
import MailIcon from '@material-ui/icons/Mail';
import VpnKeyIcon from '@material-ui/icons/VpnKey';
import Chip from '@material-ui/core/Chip';
import NotificationsIcon from '@material-ui/icons/Notifications';
import MoreIcon from '@material-ui/icons/MoreVert';
import Alert from '@material-ui/lab/Alert';
import Collapse from '@material-ui/core/Collapse'
import { utc } from 'moment';
import utils from '../utils';


export default function BookItem(props) {
  const classes = useStyles()
  console.log(props)
  if (!props.book)
    return undefined
  let book = props.book
  let tagsDom = book.info.tags.map((tag) => <Chip className={classes.bookTags} label={tag} />)
  return (
    <Card className={classes.bookCard}>
      <div style={{ width: '100%', display: 'flex', justifyContent: 'flex-start', alignItems: 'flex-start' }}>
        <Typography variant="h5" gutterBottom className={classes.headers}>
          {book.name}
        </Typography>
        <Rating value={book.info.stars} readOnly />
      </div>
      <div style={{ display: 'flex', justifyContent: 'flex-start', alignItems: 'flex-start', overflow: 'hidden' }}>
        <Typography variant="body1" style={{ maxHeight: 300 }}>
          {book.info.description}
        </Typography>
        <img src={book.info.cover} style={{ width: 180 }}></img>
      </div>
      <div style={{ display: 'flex', justifyContent: 'flex-start', alignItems: 'flex-start', overflow: 'hidden' }}>
        <Button color="primary">阅读<ArrowRightIcon /></Button>
        <Button color="primary" startIcon={<ModeCommentIcon />}>332</Button>
        {tagsDom}
      </div>
    </Card>
  )
}

const useStyles = makeStyles((theme) => ({
  bookCard: {
    padding: theme.spacing(2),
    margin: theme.spacing(1),
    // maxWidth: 300,
    maxHeight: 400,
  },
  headers: {
    color: theme.palette.primary.main
  },
  bookTags: {
    marginRight: theme.spacing(1)
  },
}))