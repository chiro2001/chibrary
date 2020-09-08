import React from 'react'
import ArrowBackIcon from '@material-ui/icons/ArrowBack';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import IconButton from '@material-ui/core/IconButton';
import Typography from '@material-ui/core/Typography';
import DehazeIcon from '@material-ui/icons/Dehaze';
import Container from '@material-ui/core/Container';
import Chip from "@material-ui/core/Chip"
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
import RefreshIcon from '@material-ui/icons/Refresh';
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
import NotificationsIcon from '@material-ui/icons/Notifications';
import MoreIcon from '@material-ui/icons/MoreVert';
import TextField from '@material-ui/core/TextField';
import Utils from "../utils.js"
import BookItem from "../components/bookItem"
// import $ from 'jquery'



function Alert(props) {
  return <MuiAlert elevation={6} variant="filled" {...props} />;
}
function ListItemLink(props) {
  return <ListItem button component="a" {...props} />;
}

let wordsDefault = undefined
let first_run = true

export default function SearchPage(props) {
  // console.log(first_run)
  function init() {
    // console.log('first_run detect...', first_run)
    if (!first_run)
      return
    first_run = false
    // console.log('firse_run true')

    window.addEventListener("popstate", function (e) {
      first_run = true
      wordsDefault = undefined
    }, false);

    let query = Utils.getQuery(props.location.search)
    // console.log('query', query)
    if (query.wd !== undefined && wordsDefault === undefined) {
      // console.log('set default')
      wordsDefault = query.wd
      setWords(wordsDefault)
    }
  }
  const classes = useStyles();
  const [state, setState] = React.useState({
    resultTags: ['轻小说', '悬疑', '文学', '轻文学', '经典'],
    resultBooks: [{
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
        cover: 'http://img.wenku8.com/image/1/1213/1213s.jpg',
        createdAt: 564238,
        lastUpdate: 254678,
        starCount: 273,
        tags: ['轻小说', '爱情', '模板']
      }
    }],
    resultUsers: [{
      username: 'chiro',
      info: {
        createdAt: 436782,
        lastLogin: 347298,
        level: 10,
        birthday: 5467383,
        gender: '♂',
        head: 'http://bed-1254016670.cos.ap-guangzhou.myqcloud.com/my_imgs/6i8ZPn__head_fin.png',
        status: 'normal'
      },
      statistics: {}
    }],
  });
  const [words, setWords] = React.useState(wordsDefault)

  init()

  let resultDomTags = state.resultTags.map((tag) => <Chip key={state.resultTags.indexOf(tag)} label={tag} style={{ margin: '1%' }} />)

  const resultPartTags = (
    <div aria-label="tags actions part">
      <Typography variant="h5" gutterBottom className={classes.headers}>
        搜索到的TAGS
      </Typography>
      <div>
        {resultDomTags}
      </div>
    </div>
  )

  let resultDomBooksItems = state.resultBooks.map((book) => <BookItem key={state.resultBooks.indexOf(book)} book={book} />)

  let resultDomBooks = (
    <div>
      <Typography variant="h5" gutterBottom className={classes.headers}>
        搜索到的书籍
      </Typography>
      {resultDomBooksItems}
    </div>
  )

  const renderPage = (
    <Container>
      <TextField id="search-box" label="书名、用户名、Tag" value={words} onChange={(event) => {
        setWords(event.target.value)
      }} fullWidth type="search" variant="outlined" />
      <br /><br />
      {resultPartTags}
      <br />
      {resultDomBooks}
    </Container>
  )

  return (
    <div className={classes.grow}>
      <AppBar position="static">
        <Toolbar>
          <IconButton
            edge="start"
            className={classes.menuButton}
            color="inherit"
            aria-label="back"
            onClick={() => { props.history.go(-1) }}
          >
            <ArrowBackIcon />
          </IconButton>
          <Typography className={classes.title} variant="h6" noWrap>
            Chibrary · 搜索
          </Typography>
          <div className={classes.grow} />
        </Toolbar>
      </AppBar>
      <br />
      {renderPage}
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
}));

