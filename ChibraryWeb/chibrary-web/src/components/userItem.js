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
  if (!props.user)
    return undefined
  let user = props.user

  return (
    <Card className={classes.userCard}>
      {/* <div style={{ width: '100%', display: 'flex', justifyContent: 'flex-start', alignItems: 'flex-start' }}>
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
      </div> */}
      <div style={{ display: 'flex', justifyContent: 'flex-start', alignItems: 'flex-start' }}>
        <img src={user.info.head} className={classes.headPhotos} />
        <div>
          <Typography variant="h6" gutterBottom className={classes.headers}>
            {user.username}
          </Typography>
          <div style={{ display: 'flex', justifyContent: 'flex-start', alignItems: 'flex-start', flexWrap: 'wrap'}}>
            <span style={{marginRight: 8}}>创建于:{utils.showTime(user.info.createdAt)}</span>
            <span style={{marginRight: 8}}>上次登录:{utils.showTime(user.info.lastLogin)}</span>
            <span style={{marginRight: 8}}>等级:{user.info.level}</span>
            <span style={{marginRight: 8}}>性别:{user.info.gender}</span>
            <span style={{marginRight: 8}}>生日:{utils.showTime(user.info.birthday)}</span>
          </div>
        </div>
      </div>
    </Card >
  )
}

const useStyles = makeStyles((theme) => ({
  headers: {
    color: theme.palette.primary.main
  },
  userCard: {
    padding: theme.spacing(2)
  },
  headPhotos: {
    borderRadius: '50%',
    width: '30vmin',
    height: '30vmin',
    objectFit: 'cover',
    objectPosition: 'center',
    maxWidth: 80,
    maxHeight: 80,
    marginRight: theme.spacing(1),
  }
}))