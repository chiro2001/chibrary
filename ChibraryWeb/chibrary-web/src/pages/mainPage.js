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
import BookItem from "../components/bookItem"
import { utc } from 'moment';
import utils from '../utils';



// function Alert(props) {
//   return <MuiAlert elevation={6} variant="filled" {...props} />;
// }
function ListItemLink(props) {
  return <ListItem button component="a" {...props} />;
}


export default function MainPage(props) {
  const classes = useStyles();
  const auth = utils.getCookie('Authorization')
  const [state, setState] = React.useState({
    isDrawerOpen: false,
    isLogin: auth === null ? false : true,
  });

  let words_search = ''

  let loginNoticeDisplayDisabled = localStorage.getItem('loginNoticeDisplayDisabled')

  const [anchorEl, setAnchorEl] = React.useState(null);
  const [mobileMoreAnchorEl, setMobileMoreAnchorEl] = React.useState(null);

  const isMenuOpen = Boolean(anchorEl);
  const isMobileMenuOpen = Boolean(mobileMoreAnchorEl);

  function closeLoginNoticeForever() {
    localStorage.setItem('loginNoticeDisplayDisabled', true)
  }

  const handleProfileMenuOpen = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleMobileMenuClose = () => {
    setMobileMoreAnchorEl(null);
  };

  const handleMenuClose = () => {
    setAnchorEl(null);
    handleMobileMenuClose();
  };

  const handleMobileMenuOpen = (event) => {
    setMobileMoreAnchorEl(event.currentTarget);
  };

  const isLoginNotice = loginNoticeDisplayDisabled ? undefined : (<div aria-label="display login notice">
    {state.isLogin ? undefined : <Alert severity="warning" action={
      <div>
        <Button color="inherit" size="small">
          登录
        </Button>
        <Button color="inherit" size="small" onClick={closeLoginNoticeForever}>
          不再显示
        </Button>
      </div>
    }>您还未登录，登录可以使用更多网站功能。</Alert>}
  </div>)

  const searchPart = (<div aria-label="search actions part">
    <Button
      variant="contained"
      size="large"
      className={classes.button}
      // startIcon={<SearchIcon />}
      // color="secondary"
      color="primary"
      style={{ borderRadius: 90, width: '100%' }}
      onClick={() => {
        props.history.push('/search')
      }}
    >
      <SearchIcon style={{ height: 60, width: 60 }} />
      <h2>找书、找用户、找tags</h2>
    </Button>
  </div>)

  const tagsPart = (
    <div aria-label="tags actions part">
      <Typography variant="h4" gutterBottom className={classes.headers}>
        流行的TAGS
      </Typography>
      <div>
        <Chip label="轻小说" style={{ margin: '1%' }} />
        <Chip label="轻文学" style={{ margin: '1%' }} />
        <Chip label="经典" style={{ margin: '1%' }} />
      </div>
    </div>
  )

  const books = []

  for (let i = 0; i < 4; i++) {
    books.push(<BookItem book={{
      name: '测试书籍',
      bid: 1,
      sources: {
        wenku8: {
          name: 'wenku8',
          username: 'chiro',
          args: {
            key: '测试书籍.epub'
          },
          data: {
            lastUpdate: 437289,
            update: '自动更新'
          }
        }
      },
      info: {
        name: '测试书籍',
        description: '这本书只是用来测试的，并没有什么特殊的，这里的字也是用来测试的。我只是想打的长一点而已。',
        author: '暗色银云',
        stars: 4,
        bid: 1,
        cover: 'http://bed-1254016670.cos.ap-guangzhou.myqcloud.com/my_imgs/MR3EcJ_place_holder.png',
        createdAt: 564238,
        lastUpdate: 254678,
        starCount: 273,
        tags: ['爱情', '模板']
      }
    }} />)
  }

  const booksPart = (
    <div aria-label="books actions part">
      <Typography variant="h4" gutterBottom className={classes.headers}>
        热门书籍
      </Typography>
      <Grid
        className={classes.booksGrid}
        spacing={2}
        container
        direction="row"
        justify="flex-start"
        alignItems="center"
      >
        {books}
      </Grid>
    </div >
  )

  const booksComentsPart = (
    <div aria-label="square actions part">
      <Typography variant="h5" gutterBottom className={classes.headers}>
        书评区
      </Typography>
    </div>
  )

  const recommendsPart = (
    <div aria-label="square actions part">
      <Typography variant="h5" gutterBottom className={classes.headers}>
        好书推荐
      </Typography>
    </div>
  )

  const waterPart = (
    <div aria-label="square actions part">
      <Typography variant="h5" gutterBottom className={classes.headers}>
        水贴区
      </Typography>
    </div>
  )

  const addPart = (
    <div aria-label="add actions part">
      <div style={{ display: 'flex', justifyContent: 'flex-start', alignItems: 'flex-start' }}>
        <Button
          variant="contained"
          size="large"
          className={classes.button}
          startIcon={<AddIcon />}
          // color="secondary"
          color="primary"
          style={{ borderRadius: 90, width: '46%' }}
        >
          新建书籍
        </Button>
        <div style={{ width: '4%' }}></div>
        <Button
          variant="contained"
          color="secondary"
          size="large"
          className={classes.button}
          startIcon={<CloudUploadIcon />}
          // color="secondary"
          style={{ borderRadius: 90, width: '46%' }}
        >
          我要上传
        </Button>
      </div>
    </div>
  )

  const squarePart = (
    <div aria-label="square actions part">
      <Typography variant="h4" gutterBottom className={classes.headers}>
        广场
      </Typography>
      {booksComentsPart}
      <br />
      {recommendsPart}
      <br />
      {waterPart}
      <br />
    </div>
  )

  const menuId = 'primary-search-account-menu';
  const renderMenu = state.isLogin ? (
    <Menu
      anchorEl={anchorEl}
      anchorOrigin={{ vertical: 'top', horizontal: 'right' }}
      id={menuId}
      keepMounted
      transformOrigin={{ vertical: 'top', horizontal: 'right' }}
      open={isMenuOpen}
      onClose={handleMenuClose}
    >
      <MenuItem onClick={handleMenuClose}>账户设置</MenuItem>
      <MenuItem onClick={handleMenuClose}>我的空间</MenuItem>
    </Menu>
  ) : (
      <Menu
        anchorEl={anchorEl}
        anchorOrigin={{ vertical: 'top', horizontal: 'right' }}
        id={menuId}
        keepMounted
        transformOrigin={{ vertical: 'top', horizontal: 'right' }}
        open={isMenuOpen}
        onClose={handleMenuClose}
      >
        <MenuItem onClick={handleMenuClose}>登录</MenuItem>
      </Menu>
    );

  const mobileMenuId = 'primary-search-account-menu-mobile';
  const renderMobileMenu = state.isLogin ? (
    <Menu
      anchorEl={mobileMoreAnchorEl}
      anchorOrigin={{ vertical: 'top', horizontal: 'right' }}
      id={mobileMenuId}
      keepMounted
      transformOrigin={{ vertical: 'top', horizontal: 'right' }}
      open={isMobileMenuOpen}
      onClose={handleMobileMenuClose}
    >
      <MenuItem>
        <IconButton aria-label="show messages" color="inherit">
          <Badge badgeContent={4} color="secondary">
            <MailIcon />
          </Badge>
        </IconButton>
        <p>信息</p>
      </MenuItem>
      {/* <MenuItem>
        <IconButton aria-label="show 11 new notifications" color="inherit">
          <Badge badgeContent={11} color="secondary">
            <NotificationsIcon />
          </Badge>
        </IconButton>
        <p>提醒</p>
      </MenuItem> */}
      <MenuItem onClick={handleProfileMenuOpen}>
        <IconButton
          aria-label="account of current user"
          aria-controls="primary-search-account-menu"
          aria-haspopup="true"
          color="inherit"
        >
          <AccountCircle />
        </IconButton>
        <p>个人主页</p>
      </MenuItem>
    </Menu>
  ) : (
      <Menu
        anchorEl={mobileMoreAnchorEl}
        anchorOrigin={{ vertical: 'top', horizontal: 'right' }}
        id={mobileMenuId}
        keepMounted
        transformOrigin={{ vertical: 'top', horizontal: 'right' }}
        open={isMobileMenuOpen}
        onClose={handleMobileMenuClose}
      >
        <MenuItem
          onClick={handleMenuClose}>
          <IconButton
            aria-label="account of current user"
            aria-controls="primary-search-account-menu"
            aria-haspopup="true"
            color="inherit"
          >
            <VpnKeyIcon />
          </IconButton>
          <p>登录</p>
        </MenuItem>
      </Menu>
    );

  return (
    <div className={classes.grow}>
      <Drawer open={state.isDrawerOpen} onClose={() => { setState(!state.isDrawerOpen) }}>
        <div style={{ width: 240 + 'px' }}>
          <List component="nav" aria-label="main mailbox folders">
            <ListItemLink button href='/index'>
              <ListItemIcon>
                <HomeIcon />
              </ListItemIcon>
              <ListItemText primary="主页" />
            </ListItemLink>
            <ListItemLink button onClick={() => { props.history.push('/search/?wd=') }}>
              <ListItemIcon>
                <SearchIcon />
              </ListItemIcon>
              <ListItemText primary="搜索" />
            </ListItemLink>
            {/* <Link to='/search/?wd='>搜索</Link> */}
            <ListItemLink button onClick={() => { props.history.push('/search/?wd=') }}>
              <ListItemIcon>
                <ModeCommentIcon />
              </ListItemIcon>
              <ListItemText primary="书评区" />
            </ListItemLink>
            <ListItemLink button onClick={() => { props.history.push('/search/?wd=') }}>
              <ListItemIcon>
                <ThumbUpIcon />
              </ListItemIcon>
              <ListItemText primary="好书推荐" />
            </ListItemLink>
            <ListItemLink button onClick={() => { props.history.push('/search/?wd=') }}>
              <ListItemIcon>
                <ForumIcon />
              </ListItemIcon>
              <ListItemText primary="水贴区" />
            </ListItemLink>

            <ListItemLink button href='https://gitee.com/chiro2001/chibrary'>
              <ListItemIcon>
                <GitHubIcon />
              </ListItemIcon>
              <ListItemText primary="关于" />
            </ListItemLink>
          </List>
        </div>
      </Drawer>
      <AppBar position="static">
        <Toolbar>
          <IconButton
            edge="start"
            className={classes.menuButton}
            color="inherit"
            aria-label="open drawer"
            onClick={() => { setState({ isDrawerOpen: !state.isDrawerOpen }) }}
          >
            <MenuIcon />
          </IconButton>
          <Typography className={classes.title} variant="h6" noWrap>
            Chibrary · 主页
          </Typography>
          <div className={classes.search}>
            <div className={classes.searchIcon}>
              <SearchIcon />
            </div>
            <InputBase
              placeholder="搜索"
              classes={{
                root: classes.inputRoot,
                input: classes.inputInput,
              }}
              inputProps={{ 'aria-label': 'search' }}
              fullWidth
              onChange={(event) => { words_search = event.target.value }}
              onKeyDown={(event) => {
                if (event.key === 'Enter') {
                  console.log('Search', words_search)
                  props.history.push('/search/?wd=' + words_search)
                }
              }}
            />
          </div>
          <div className={classes.grow} />
          <div className={classes.sectionDesktop}>
            <IconButton aria-label="show 4 new mails" color="inherit">
              <Badge badgeContent={4} color="secondary">
                <MailIcon />
              </Badge>
            </IconButton>
            {/* <IconButton aria-label="show 17 new notifications" color="inherit">
              <Badge badgeContent={17} color="secondary">
                <NotificationsIcon />
              </Badge>
            </IconButton> */}
            <IconButton
              edge="end"
              aria-label="account of current user"
              aria-controls={menuId}
              aria-haspopup="true"
              onClick={handleProfileMenuOpen}
              color="inherit"
            >
              <AccountCircle />
            </IconButton>
          </div>
          <div className={classes.sectionMobile}>
            <IconButton
              aria-label="show more"
              aria-controls={mobileMenuId}
              aria-haspopup="true"
              onClick={handleMobileMenuOpen}
              color="inherit"
            >
              <MoreIcon />
            </IconButton>
          </div>
        </Toolbar>
      </AppBar>
      {renderMobileMenu}
      {renderMenu}
      <br />
      <Container>
        <div>
          {isLoginNotice}
        </div>
        <br />
        <div>
          {searchPart}
        </div>
        <br />
        <div>
          {tagsPart}
        </div>
        <br />
        <div>
          {booksPart}
        </div>
        <br />
        <div>
          {addPart}
        </div>
        <br />
        <div>
          {squarePart}
        </div>
      </Container>
    </div>
  );
}



const useStyles = makeStyles((theme) => ({
  grow: {
    flexGrow: 1,
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
  booksGrid: {

  },
  bookCard: {
    padding: theme.spacing(2),
    margin: theme.spacing(1),
    maxWidth: 300,
    maxHeight: 400,
  },
  headers: {
    color: theme.palette.primary.main
  },
  title: {
    display: 'none',
    [theme.breakpoints.up('sm')]: {
      display: 'block',
    },
  },
  search: {
    position: 'relative',
    borderRadius: theme.shape.borderRadius,
    backgroundColor: fade(theme.palette.common.white, 0.15),
    '&:hover': {
      backgroundColor: fade(theme.palette.common.white, 0.25),
    },
    marginRight: theme.spacing(2),
    marginLeft: 0,
    width: '100%',
    [theme.breakpoints.up('sm')]: {
      marginLeft: theme.spacing(3),
      width: 'auto',
    },
  },
  searchIcon: {
    padding: theme.spacing(0, 2),
    height: '100%',
    position: 'absolute',
    pointerEvents: 'none',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
  },
  inputRoot: {
    color: 'inherit',
  },
  inputInput: {
    padding: theme.spacing(1, 1, 1, 0),
    // vertical padding + font size from searchIcon
    paddingLeft: `calc(1em + ${theme.spacing(4)}px)`,
    transition: theme.transitions.create('width'),
    width: '100%',
    [theme.breakpoints.up('md')]: {
      width: '20ch',
    },
  },
  sectionDesktop: {
    display: 'none',
    [theme.breakpoints.up('md')]: {
      display: 'flex',
    },
  },
  sectionMobile: {
    display: 'flex',
    [theme.breakpoints.up('md')]: {
      display: 'none',
    },
  },
}));

