# UBI Discussion - Discord Archive

A static Discord clone built with Astro to preserve and display UBI (Universal Basic Income) discussions from a Discord server that was at risk of disappearing.

## 🎯 Project Purpose

This project serves as a digital archive for important discussions about Universal Basic Income, preserving valuable conversations, research, and policy insights in a familiar Discord-like interface.

## ✨ Features

- **Discord-like Interface** - Familiar 3-column layout with server bar, channel sidebar, and user list
- **Message Archive** - Complete conversation history with timestamps, reactions, and user avatars
- **Static Site** - Fast loading, no backend required, perfect for long-term preservation
- **Responsive Design** - Works on desktop and mobile devices
- **Searchable Content** - All text content is indexed and searchable

## 🏗️ Architecture

- **Frontend**: Astro (Static Site Generation)
- **Styling**: Tailwind CSS
- **Data**: Static JSON files
- **Deployment**: Any static hosting service

## 📁 Project Structure

```
/
├── src/
│   ├── components/
│   │   ├── DiscordLayout.astro    # Main Discord interface
│   │   └── Message.astro          # Individual message component
│   ├── data/
│   │   └── messages.json          # UBI discussion data
│   ├── layouts/
│   │   └── Layout.astro           # Base HTML layout
│   └── pages/
│       └── index.astro            # Main page
├── public/                        # Static assets
└── package.json
```

## 🚀 Getting Started

### Prerequisites

- Node.js 18.20.8 or higher
- npm or yarn

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Beta-Techno/hive.git
cd hive
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

4. Open [http://localhost:4321](http://localhost:4321) in your browser

### Build for Production

```bash
npm run build
```

The built site will be in the `dist/` directory, ready for deployment.

## 📊 Data Structure

Messages are stored in `src/data/messages.json` with the following structure:

```json
{
  "messages": [
    {
      "id": "1",
      "author": "Username",
      "content": "Message content",
      "timestamp": "Today at 2:30 PM",
      "avatar": "A",
      "isEdited": false,
      "reactions": [
        { "emoji": "👍", "count": 3 }
      ]
    }
  ]
}
```

## 🎨 Customization

### Adding New Messages

1. Edit `src/data/messages.json`
2. Add new message objects following the existing structure
3. Rebuild the site

### Styling Changes

- Main Discord styling is in `src/components/DiscordLayout.astro`
- Message styling is in `src/components/Message.astro`
- Global styles are in `src/layouts/Layout.astro`

### Adding New Channels

1. Update the channel list in `DiscordLayout.astro`
2. Create new pages for each channel in `src/pages/`
3. Add corresponding message data

## 🌐 Deployment

This static site can be deployed to any hosting service:

- **Netlify**: Drag and drop the `dist/` folder
- **Vercel**: Connect your GitHub repository
- **GitHub Pages**: Enable Pages in repository settings
- **AWS S3**: Upload files to an S3 bucket

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Built with [Astro](https://astro.build)
- Styled with [Tailwind CSS](https://tailwindcss.com)
- Inspired by Discord's interface design
- Preserving important discussions about Universal Basic Income

---

**Note**: This archive preserves discussions that were at risk of being lost. The content represents real conversations about UBI policy and implementation.
